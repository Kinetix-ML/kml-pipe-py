from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.base_structs import DataType
from KMLPipePy.types import Keypoint2D, KPFrame, Canvas, Annotation
import math

class KPDist(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """

    def calcDist(p1 : Keypoint2D, p2: Keypoint2D):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


    def execute(self):
        kp1 : Keypoint2D = self.vars[self.cvnode.inputs[0].connection.id]
        kp2 : Keypoint2D = self.vars[self.cvnode.inputs[1].connection.id]

        if (kp1 == DataType.NoDetections or
            kp2 == DataType.NoDetections):
            self.vars[self.cvnode.outputs[0].id] = DataType.NoDetections;
            return
        self.vars[self.cvnode.outputs[0].id] = KPDist.calcDist(kp1, kp2)