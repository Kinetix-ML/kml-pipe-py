from KMLPipePy import KMLPipeline
from KMLPipePy.types import Canvas
import cv2
import time

pipe = KMLPipeline("Python Pipe Test", 1, "59b94abb-9138-43e5-8926-cc9b55c38e7c")
pipe.initialize()

out = Canvas()
cam = cv2.VideoCapture(0)

while True:
  res, image = cam.read()
  
  if image is not None and image.any():
    out.set_image(image)
    t0 = time.time()
    pipe.execute([image, out])
    t1 = time.time()
    print(f"{1/(t1-t0)} fps")

    if out.show(1):
      break

cam.release()