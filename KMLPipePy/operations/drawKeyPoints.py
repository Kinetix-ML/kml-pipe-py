from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.types import Keypoint2D, KPFrame, Canvas, Annotation
from numpy import ndarray

class DrawKeyPoints(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """
        self.radius = self.cvnode.parameters[0].value

    def execute(self):
        keypoints : KPFrame = self.vars[self.cvnode.inputs[0].connection.id]
        image : ndarray = self.vars[self.cvnode.inputs[1].connection.id]
        canvas : Canvas = self.vars[self.cvnode.inputs[2].connection.id]

        # BGR
        COLOR = (255, 255, 255)

        canvas.set_image(image)
        annotations = [Annotation(kp.x, kp.y, self.radius, COLOR) for kp in keypoints.keypoints]
        canvas.add_annotations(annotations)