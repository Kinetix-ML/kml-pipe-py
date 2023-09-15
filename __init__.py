from base_structs import Project, Version, CVPipeline, CVNode
from CVNodeProcess import CVNodeProcess
from operations import NodeCatalog
from typing import List, Dict
from api import get_project_version
import asyncio

class KMLPipeline:
    projectName: str
    projectVersion: int
    apiKey: str
    project: Project | None
    version: Version | None
    pipeline: CVPipeline | None
    nodes: List[CVNode] | None
    execNodes: Dict[str, CVNodeProcess] = []
    vars: Dict[str, any] = []

    def __init__(self, projectName, projectVersion, apiKey):
        self.projectName = projectName
        self.projectVersion = projectVersion
        self.apiKey = apiKey

    def load_config(self, project, version):
        self.project = project
        self.version = version

    async def initialize(self):
        # get project and version details from firebase
        if not self.project or not self.version:
            project, version = get_project_version(
                self.projectName, self.projectVersion, self.apiKey
            )
            self.project = project
            self.version = version

        self.pipeline = self.version.pipeline
        self.nodes = self.version.pipeline.nodes

        for node in [n for n in self.pipeline.nodes if n.id not in self.exec_nodes]:
            new_exec_node = NodeCatalog[node.operation](node, self.vars)
            new_exec_node.initialize()
            self.exec_nodes[node.id] = new_exec_node

    async def execute(self, input_values):
        if len(input_values) != len(self.pipeline.inputs):
            expected = len(self.pipeline.inputs)
            given = len(input_values)
            raise ValueError(f"[Pipeline Execution Error] Incorrect Number of Inputs. Expected: {expected} but got: {given}")

        clear_vars(self.vars)

        for i, value in enumerate(input_values):
            self.vars[self.pipeline.inputs[i].id] = value  # assumed as CVImage

        executed_nodes = []
        ready_nodes = check_ready_nodes(self.nodes, executed_nodes, self.vars)

        if not ready_nodes:
            raise ValueError("No Nodes to Execute")

        while ready_nodes:
            [node.execute() for node in ready_nodes]
            executed_nodes.extend(ready_nodes)
            ready_nodes = check_ready_nodes(self.nodes, executed_nodes, self.vars)

        return [
            {**output, "value": self.vars.get(output.connection.id, None)}
            for output in self.pipeline.outputs if output.connection
        ]


def clear_vars(vars):
    for key in vars:
        vars[key] = None


def check_ready_nodes(nodes, executed_nodes, vars):
    return [
        node for node in nodes
        if node.label not in [n.label for n in executed_nodes] and
        all(input.connection and input.connection.id in vars for input in node.inputs)
    ]