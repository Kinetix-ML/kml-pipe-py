import requests
import json
from KMLPipePy.base_structs import Project, Version, CVNode, CVParameter, CVVariableConnection, CVVariable  # assuming base_structs is a Python module containing the definitions

def get_project_version(project_name: str, project_version: int, api_key: str):
    url = f"https://getpipeline-kk2bzka6nq-uc.a.run.app/?projectName={project_name}&version={project_version}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # this will raise an HTTPError if the HTTP request returned an unsuccessful status code

    res_json = response.json()
    print(res_json)
    p = res_json["project"]
    project = Project(p["id"], p["projectName"], p["owner"], p["versions"])#json.loads(json.dumps(res_json["project"]), object_hook=Project)
    v = res_json["version"]
    params = parse_params(v["pipeline"]["parameters"])
    inputs = parse_inputs(v["pipeline"]["inputs"])
    pipe = []
    for node in v["nodes"]:


        outputs = parse_outputs(node["outputs"])
        cvnode = CVNode(node["id"], node["label"], node["operation"], params, inputs, outputs, node["platforms"])
        pipe.append(cvnode)
    version = Version(v["id"], v["projectID"], v["version"], pipe)#json.loads(json.dumps(res_json["version"]), object_hook=Version)
    # Assuming that Project and Version classes or dataclasses have a way to parse from dict or you just want to keep them as dict
    return (
        project,
        version,
    )

def parse_params(params):
    res = []
    for param in params:
        res.append(CVParameter(param["name"], param["label"], param["dataType"], param["value"]))
    return res

def parse_inputs(inputs):
    res = []
    for input in inputs:
        c = input["connection"]
        connection = CVVariable(c["id"], c["name"], c["dataType"], None)

        res.append(CVVariableConnection(input["id"], connection, input["dataType"]))
    return res

def parse_outputs(outputs):
    res = []
    for output in outputs:
        res.append(CVVariable(output["id"], output["name"], output["dataType"], None))
    return res

# Note: If Project and Version have some parsing methods, you might need to invoke them to convert res_json["project"] and res_json["version"] to respective types.