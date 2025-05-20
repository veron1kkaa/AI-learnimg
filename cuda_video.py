import torch
import cv2

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Використовується пристрій: {device}")

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
model.to(device)

video_path = r"C:\Users\Student\Downloads\video_example.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Не вдалося відкрити відео")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = model(img_rgb)

    annotated_frame = results.render()[0]

    cv2.imshow("YOLOv5 Detection", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
