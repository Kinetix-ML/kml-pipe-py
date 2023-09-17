from KMLPipePy import KMLPipeline

# create pipeline
pipe = KMLPipeline("Python Test", 1, "79705c77-f57b-449d-b856-03138e8859a7")

# initialize
pipe.initialize()

# execute
outputs = pipe.execute([1, 2])

# print output
print(outputs)