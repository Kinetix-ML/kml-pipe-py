from typing import Dict
from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.operations.addInputs import AddInputs

NodeCatalog: Dict[str,CVNodeProcess] = {"AddInputs": AddInputs}