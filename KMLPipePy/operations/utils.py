import math
from KMLPipePy.types import Keypoint2D

def calcKPDist(p1 : Keypoint2D, p2: Keypoint2D):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)