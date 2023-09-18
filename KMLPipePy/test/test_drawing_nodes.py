import unittest
from KMLPipePy.operations.pose2D import Pose2D
from KMLPipePy.operations.drawKeyPoints import DrawKeyPoints
from KMLPipePy.base_structs import CVNode, CVVariable, CVVariableConnection, CVParameter
from KMLPipePy.types import Canvas
import cv2
import time

# python -m unittest

class TestModelNodes(unittest.TestCase):
    DO_TEST = True

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

        return res

    def test_pose2d(self):
        if not self.DO_TEST:
            return
        image = cv2.imread("./KMLPipePy/test/test_media/testimage.jpeg")
        image = cv2.resize(image, (400, 600))

        node1 = self.__construct_node__(Pose2D, [image], 1, [])
        node1.execute()

        res = node1.vars["output-0"]

        out = Canvas(None)
        node2 = self.__construct_node__(DrawKeyPoints, [res, image, out], 0, [10])
        
        node2.execute()
        out.show(0)
        out.close()

        cam = cv2.VideoCapture(0)

        prevTime = 0

        while True:
            result, image = cam.read()
            node1.vars["input-0"] = image
            node1.execute()
            res = node1.vars["output-0"]

            node2.vars["input-0"] = res
            node2.vars["input-1"] = image
            node2.execute()
            out.show(1)

            curr = time.time()
            delta = curr - prevTime
            prevTime = curr
            print(f"{round(1 / delta)} fps")
        
        out.close()