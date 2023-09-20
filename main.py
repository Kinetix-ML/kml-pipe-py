from KMLPipePy import KMLPipeline
from KMLPipePy.types import Canvas
import cv2

pipe = KMLPipeline("Python Pipe Test", 1, "59b94abb-9138-43e5-8926-cc9b55c38e7c")
pipe.initialize()

out = Canvas()
cam = cv2.VideoCapture(0)

while True:
  res, image = cam.read()
  out.set_image(image)
  pipe.execute([image, out])

  if out.show(1):
    break

cam.release()