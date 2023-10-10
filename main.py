from KMLPipePy import KMLPipeline
from KMLPipePy.types import Canvas
import cv2
import time
import time

pipe = KMLPipeline("Roboflow Test", 2, "261e97fd-18b1-4a3c-8cc1-b94a421c11bf")
pipe.initialize()
print("Done Initializing")

out = Canvas()
cam = cv2.VideoCapture(1)
print("Starting Capture")

while True:
  res, image = cam.read()
  print("Read Frame")

  if image is not None and image.any():
    out.set_image(image)
    t0 = time.time()
    outputs = pipe.execute([image, out])
    print(outputs)
    t1 = time.time()
    print(f"{1/(t1-t0)} fps")

    if out.show(1):
      break

cam.release()