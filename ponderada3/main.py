from ultralytics import YOLO
from PIL import Image

# load a model
model = YOLO('yolov8n.pt')

# Train the model
model.train(data='data.yaml', epochs=2)
model.val()

# Link for inputs
inp_1 = Image.open("test/images/1616.rf.c868709931a671796794fdbb95352c5a.jpg")
inp_2 = Image.open("datasets/test/images/1675.rf.e3aa3f8d28d0247ef0284dd46dacc29f.jpg")
inp_3 = Image.open("datasets/test/images/1686.rf.809fb1b51c607e5cf787e44ef4ddd7b8.jpg")
inps = [inp_1, inp_2, inp_3]

# Analyze the inputs, show and save them
for inp in inps:
	model.predict(source=inp, show=True, save=True)
