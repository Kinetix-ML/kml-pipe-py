from dataclasses import dataclass
from numpy import ndarray
import cv2
from enum import Enum

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

@dataclass
class BBox:
    x: int
    y: int
    width: int
    height: int
    color: (int, int, int)
    label: str
    confidence: float

class Canvas:
    FONT = cv2.FONT_HERSHEY_PLAIN
    FONT_SIZE = 1
    THICKNESS = 2

    image : ndarray = None
    def __init__(self, image : ndarray = None):
        self.image = image
    
    def add_annotations(self, annotations : list[Annotation]):
        self.annotations = annotations
        for dot in annotations:
            cv2.circle(self.image, (dot.x, dot.y), 0, dot.color, dot.radius)

    def add_bboxes(self, bboxes: list[BBox]):
        self.bboxes = bboxes
        for bbox in bboxes:
            cv2.rectangle(img=self.image,
                pt1=(int(bbox.x - (bbox.width // 2)), int(bbox.y - (bbox.height // 2))),
                pt2=(int(bbox.x + (bbox.width // 2)), int(bbox.y + (bbox.height // 2))),
                color=bbox.color, thickness=self.THICKNESS)
            cv2.putText(self.image, bbox.label,
                        (int(bbox.x - (bbox.width // 2)), int(bbox.y - (bbox.height // 2) - 2 * self.THICKNESS)),
                        self.FONT, self.FONT_SIZE, bbox.color, 1)
    
    def set_image(self, image):
        self.annotations = None
        self.image = image.copy()

    def show(self, time : int):
        cv2.imshow("Image", self.image)
        return cv2.waitKey(time) & 0xFF == 27 # exit with esc
    
    def close(self):
        cv2.destroyAllWindows()