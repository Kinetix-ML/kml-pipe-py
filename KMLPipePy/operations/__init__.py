from typing import Dict
from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.operations.addInputs import AddInputs
from KMLPipePy.operations.divideInputs import DivideInputs
from KMLPipePy.operations.multiplyInputs import MultiplyInputs
from KMLPipePy.operations.subtractInputs import SubtractInputs
from KMLPipePy.operations.constant import Constant
from KMLPipePy.operations.round import Round
from KMLPipePy.operations.clamp import Clamp

NodeCatalog: Dict[str,CVNodeProcess] = {
    "AddInputs": AddInputs,
    "DivideInputs": DivideInputs,
    "MultiplyInputs": MultiplyInputs,
    "SubtractInputs": SubtractInputs,
    "Constant": Constant,
    "Round": Round,
    "Clamp": Clamp
}