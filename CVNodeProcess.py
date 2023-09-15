from base_structs import CVNode
from typing import Dict

class CVNodeProcess:
    cvnode: CVNode
    vars: Dict[str, any]

    def __init__(self, cvnode: CVNode, vars: Dict[str, any]):
        self.cvnode = cvnode
        self.vars = vars

    def initialize(self):
        """
        Should be overridden
        :return:
        """

    def execute(self):
        """
        Should be overridden
        :return:
        """
