import yt_dlp
import cv2
import torch
import warnings
import time

warnings.filterwarnings("ignore", category=FutureWarning)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Використовується пристрій: {device}")
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
model.to(device)

youtube_url = "https://www.youtube.com/watch?v=Lcdi9O2XB4E"

ydl_opts = {
    'quiet': True,
    'format': 'best[protocol^=m3u8]',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    video_url = info_dict.get("url", None)

cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Не вдалося відкрити стрім")
    exit()

log_file = "detection_log.txt"
with open(log_file, "w", encoding="utf-8") as log:
    log.write("Object detection log:\n")

print("Розпізнавання почалось. Натисни ESC для виходу.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Потік завершився або не читається.")
        break

    timestamp_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
    timestamp_sec = int(timestamp_ms // 1000)
    minutes = timestamp_sec // 60
    seconds = timestamp_sec % 60

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)
    annotated_frame = results.render()[0]

    predictions = results.pred[0]
    labels = results.names

    for *box, conf, cls in predictions:
        label = labels[int(cls)]
        conf_value = float(conf)
        text = f"[{minutes:02}:{seconds:02}] Detected: {label} ({conf_value:.2f})"
        print(text)
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(text + "\n")

    cv2.imshow("YouTube YOLOv5 Detection", annotated_frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
print("Роботу завершено.")
