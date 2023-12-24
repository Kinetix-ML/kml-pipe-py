from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.types import Keypoint2D, KPFrame
from KMLPipePy.base_structs import DataType

from rtmlib.tools import Wholebody
import torch
import cv2
import numpy as np

LABELS = ["nose"," left eye"," right eye"," left ear"," right ear"," left shoulder"," right shoulder"," left elbow"," right elbow"," left wrist"," right wrist"," left hip"," right hip"," left knee"," right knee"," left ankle"," right ankle"]

class RTMPose2DWholeBody(CVNodeProcess):

    def initialize(self):
        """
        Initialization code
        :return:
        """
        device = 'cpu'  # cpu, cuda
        if torch.cuda.is_available():
            device = 'cuda'

        backend = 'onnxruntime'  # opencv, onnxruntime, openvino

        openpose_skeleton = False  # True for openpose-style, False for mmpose-style

        self.model = Wholebody(to_openpose=openpose_skeleton,
                            mode='balanced',  # 'performance', 'lightweight', 'balanced'. Default: 'balanced'
                            backend=backend, device=device)

    def execute(self):
        image = self.vars[self.cvnode.inputs[0].connection.id]

        if self.catchNoDetections(image):
            self.vars[self.cvnode.outputs[0].id] = DataType.NoDetections
            return

        keypoints, scores = self.model(image)

        if (keypoints.shape[0] == 0):
            self.vars[self.cvnode.outputs[0].id] = DataType.NoDetections
            return
        
        keypoints = keypoints[0].reshape(keypoints.shape[1], keypoints.shape[2])
        scores = scores[0].flatten()

        out = KPFrame(keypoints=[Keypoint2D(x = int(p[0]), y = int(p[1]), score = scores[i], name = i)
                for i, p in enumerate(keypoints)])

        self.vars[self.cvnode.outputs[0].id] = out