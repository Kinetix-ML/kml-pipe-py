from dataclasses import dataclass
from numpy import ndarray
import cv2

@dataclass
class Keypoint2D:
    x: int
    y: int
    score: float
    name: str


@dataclass
class KPFrame:
    keypoints: list[Keypoint2D]

@dataclass
class Annotation:
    x: int
    y: int
    radius: int
    color: (int, int, int)

class Canvas:
    image : ndarray = None
    def __init__(self, image : ndarray = None):
        self.image = image
    
    def add_annotations(self, annotations : list[Annotation]):
        self.annotations = annotations
        for dot in annotations:
            self.image = cv2.circle(self.image, (dot.x, dot.y), 0, dot.color, dot.radius)
    
    def set_image(self, image):
        self.annotations = None
        self.image = image.copy()

    def show(self, time : int):
        cv2.imshow("Image", self.image)
        return cv2.waitKey(time) & 0xFF == 27 # exit with esc
    
    def close(self):
        cv2.destroyAllWindows()