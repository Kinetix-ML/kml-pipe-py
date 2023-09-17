from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.base_structs import DataType
class GetVecValue(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """

    def execute(self):
        vec = self.vars[self.cvnode.inputs[0].connection.id]
        index = self.vars[self.cvnode.inputs[1].connection.id]

        if vec == DataType.NoDetections:
            self.vars[self.cvnode.outputs[0].id] = DataType.NoDetections
            return

        if index == DataType.NoDetections:
            self.vars[self.cvnode.outputs[0].id] = DataType.NoDetections
            return
        
        
        self.vars[self.cvnode.outputs[0].id] = vec[index]