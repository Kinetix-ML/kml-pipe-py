from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.base_structs import DataType
from KMLPipePy.types import Keypoint2D, KPFrame, Canvas, Annotation
import math

class ThreeKPAngle(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """
    
    def calc3PtAngle(p1 : Keypoint2D, p2: Keypoint2D, p3: Keypoint2D):
        # https://stackoverflow.com/a/31334882
        part1 = math.atan2(p3.y - p2.y, p3.x - p2.x)
        part2 = math.atan2(p1.y - p2.y, p1.x - p2.x)

        return abs(part1 - part2) * (180 / math.pi)

    def execute(self):
        kp1 : Keypoint2D = self.vars[self.cvnode.inputs[0].connection.id]
        kp2 : Keypoint2D = self.vars[self.cvnode.inputs[1].connection.id]
        kp3 : Keypoint2D = self.vars[self.cvnode.inputs[2].connection.id]

        if self.catchNoDetections(kp1, kp2, kp3):
            return
        
        self.vars[self.cvnode.outputs[0].id] = ThreeKPAngle.calc3PtAngle(kp1, kp2, kp3)