import math
from KMLPipePy.types import Keypoint2D
from KMLPipePy.base_structs import DataType

def calc3PtAngle(p1 : Keypoint2D, p2: Keypoint2D, p3: Keypoint2D):
    # https://stackoverflow.com/a/31334882
    part1 = math.atan2(p3.y - p2.y, p3.x - p2.x)
    part2 = math.atan2(p1.y - p2.y, p1.x - p2.x)

    return abs(part1 - part2) * (180 / math.pi)

def calcKPDist(p1 : Keypoint2D, p2: Keypoint2D):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
