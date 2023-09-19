import unittest
import math
from KMLPipePy.operations.threeKPAngle import ThreeKPAngle 
from KMLPipePy.operations.kpDist import KPDist
from KMLPipePy.operations.smoothKeyPoints import SmoothKeyPoints
from KMLPipePy.base_structs import CVNode, CVVariable, CVVariableConnection, CVParameter
from KMLPipePy.types import Keypoint2D, KPFrame

class TestMathNodes(unittest.TestCase):
    def __construct_node__(self, node, inputs : list, num_outputs : int, parameters : list):
        cv_node = CVNode(
            parameters = [
                CVParameter(name=None, label=None, dataType=None, value=x) for x in parameters
            ],
            inputs = [
                CVVariableConnection(connection=CVVariable(id = "input-" + str(x),
                                    name=None, dataType=None, value=None),
                                    id=None, dataType=None) for x in range(len(inputs))],
            outputs = [CVVariable(id = "output-" + str(x), name=None, value=None, dataType=None)
                       for x in range(num_outputs)],
            id=None, label=None, operation=None, platforms=None)
            
        vars = {}
        for i, input in enumerate(inputs):
            vars["input-" + str(i)] = input
        for i in range(num_outputs):
            vars["output-" + str(i)] = None

        res = node(cv_node, vars)
        res.initialize()
        res.execute()

        return res

    def test_3pt_angle(self):
        kp1 = Keypoint2D(x=1, y=1, score=None, name=None)
        kp2 = Keypoint2D(x=0, y=0, score=None, name=None)
        kp3 = Keypoint2D(x=1, y=0, score=None, name=None)
        node = self.__construct_node__(ThreeKPAngle, [kp1, kp2, kp3], 1, [])
        self.assertEqual(node.vars["output-0"], 45)
        
        kp1.x = 0
        node = self.__construct_node__(ThreeKPAngle, [kp1, kp2, kp3], 1, [])
        self.assertEqual(node.vars["output-0"], 90)

        kp1.x = -1
        node = self.__construct_node__(ThreeKPAngle, [kp1, kp2, kp3], 1, [])
        self.assertEqual(node.vars["output-0"], 135)

    def test_kp_dist(self):
        kp1 = Keypoint2D(x=2, y=4, score=None, name=None)
        kp2 = Keypoint2D(x=1, y=3, score=None, name=None)
        node = self.__construct_node__(KPDist, [kp1, kp2], 1, [])
        self.assertEqual(node.vars["output-0"], math.sqrt(2))
    
    def test_smooth_kps(self):
        kp1 = Keypoint2D(x=0, y=0, score=1, name="a")
        kp2 = Keypoint2D(x=1, y=1, score=1, name="b")
        
        kpa = Keypoint2D(x=1, y=1, score=0.5, name="a")
        kpb = Keypoint2D(x=1, y=1, score=0.5, name="b")

        frame1 = KPFrame(keypoints=[kp1, kp2])
        frame2 = KPFrame(keypoints=[kpa, kpb])

        node = self.__construct_node__(SmoothKeyPoints, [frame1], 1, [5])

        node.vars["input-0"] = frame2
        node.execute()
        node.execute()
        node.execute()
        node.execute()
        node.execute()