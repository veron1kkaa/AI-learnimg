import torch
from matplotlib import pyplot as plt
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img_path = r'C:\Users\Student\Downloads\images.jpg'
img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

results = model(img_rgb)

results.show()

labels = results.names
predictions = results.pred[0]
for *box, conf, cls in predictions:
    label = labels[int(cls)]
    print(f"Detected {label} with confidence {conf:.2f}")

results.save()
