from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.base_structs import DataType
class Switch(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """

    def execute(self):
        boolean = self.vars[self.cvnode.inputs[0].connection.id]
        passthrough = self.vars[self.cvnode.inputs[1].connection.id]

        self.vars[self.cvnode.outputs[0].id] = passthrough if boolean else DataType.NoDetections
