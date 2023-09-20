from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.base_structs import DataType
from KMLPipePy.types import KPFrame, Keypoint2D

class CreateKeyPoint(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """

    def execute(self):
        x : int = self.vars[self.cvnode.inputs[0].connection.id]
        y : int = self.vars[self.cvnode.inputs[1].connection.id]
        score : float = self.vars[self.cvnode.inputs[2].connection.id]
        name : str = self.vars[self.cvnode.inputs[3].connection.id]

        if x == DataType.NoDetections or y == DataType.NoDetections or score == DataType.NoDetections or name == DataType.NoDetections:
            return

        self.vars["output-0"] = Keypoint2D(x = x, y = y, score = score, name = name)