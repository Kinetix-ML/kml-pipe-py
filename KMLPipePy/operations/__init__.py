from typing import Dict
from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.operations.addInputs import AddInputs
from KMLPipePy.operations.divideInputs import DivideInputs
from KMLPipePy.operations.multiplyInputs import MultiplyInputs
from KMLPipePy.operations.subtractInputs import SubtractInputs
from KMLPipePy.operations.constant import Constant
from KMLPipePy.operations.round import Round
from KMLPipePy.operations.clamp import Clamp
from KMLPipePy.operations.getVecValue import GetVecValue
from KMLPipePy.operations.setVecValue import SetVecValue
from KMLPipePy.operations.smoothVecs import SmoothVecs
from KMLPipePy.operations.conditional import Conditional
from KMLPipePy.operations.switch import Switch
from KMLPipePy.operations.pose2D import Pose2D
from KMLPipePy.operations.drawKeyPoints import DrawKeyPoints

NodeCatalog: Dict[str,CVNodeProcess] = {
    "AddInputs": AddInputs,
    "DivideInputs": DivideInputs,
    "MultiplyInputs": MultiplyInputs,
    "SubtractInputs": SubtractInputs,
    "Constant": Constant,
    "Round": Round,
    "Clamp": Clamp,
    "GetVecValues": GetVecValue,
    "SetVecValues": SetVecValue,
    "SetVecValues": SmoothVecs,
    "Conditional": Conditional,
    "Switch": Switch,
    "Pose2D": Pose2D,
    "DrawKeyPoints": DrawKeyPoints
}