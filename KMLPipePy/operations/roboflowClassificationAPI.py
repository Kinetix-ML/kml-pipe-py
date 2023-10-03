from KMLPipePy.CVNodeProcess import CVNodeProcess
from KMLPipePy.types import BBox

from roboflow import Roboflow

class RoboflowClassificationAPI(CVNodeProcess):
    def initialize(self):
        """
        Initialization code
        :return:
        """
        model_name = self.cvnode.parameters[0].value
        version = self.cvnode.parameters[1].value
        api_key = self.cvnode.parameters[2].value

        rf = Roboflow(api_key=api_key)
        project = rf.workspace().project(model_name)
        self.model = project.version(version).model

    def execute(self):
        images = self.vars[self.cvnode.inputs[0].connection.id]

        if self.catchNoDetections(images):
            return

        out = []
        for image in images:
            out.append(self.model.predict(image))
        print(out)
        
        self.vars[self.cvnode.outputs[0].id] = out