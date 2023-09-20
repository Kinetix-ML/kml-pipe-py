from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.base_structs import DataType
from KMLPipePy.types import KPFrame

class GetKeyPoint(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """
        self.index : int = self.cvnode.parameters[0].value

    def execute(self):
        kp : KPFrame = self.vars[self.cvnode.inputs[0].connection.id]

        if kp == DataType.NoDetections:
            self.vars[self.cvnode.outputs[0].id] = DataType.NoDetections
            return
        
        self.vars[self.cvnode.outputs[0].id] = kp.keypoints[self.index]