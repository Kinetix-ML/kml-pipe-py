from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.base_structs import DataType
from KMLPipePy.types import Keypoint2D, KPFrame, Canvas, Annotation
from .utils import calcKPDist

class KPDist(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """

    def execute(self):
        kp1 : Keypoint2D = self.vars[self.cvnode.inputs[0].connection.id]
        kp2 : Keypoint2D = self.vars[self.cvnode.inputs[1].connection.id]

        if (kp1 == DataType.NoDetections or
            kp2 == DataType.NoDetections):
            self.vars[self.cvnode.outputs[0].id] = DataType.NoDetections;
            return
        self.vars[self.cvnode.outputs[0].id] = calcKPDist(kp1, kp2)