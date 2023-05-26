from ultralytics import YOLO

# build a new model from YAML
model = YOLO('yolov8n.pt')

# Train the model
model.train(data='data.yaml', epochs=1, imgsz=416)

inputs = ["test/images/1616.rf.c868709931a671796794fdbb95352c5a.jpg", "test/images/1675.rf.e3aa3f8d28d0247ef0284dd46dacc29f.jpg"]  # list

for input in inputs:
    model(inputs)
