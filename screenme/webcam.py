import csv
import os
import time

import cv2
from EmoPy.src.fermodel import FERModel

IMAGE_DIR = os.path.expanduser("~/screenme")
CSV_PATH = os.path.join(IMAGE_DIR, "emotion.csv")


def capture_webcam_image(save_path=IMAGE_DIR):
    image_path = os.path.join(IMAGE_DIR, "webcam.png")

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(image_path, frame)
    cap.release()

    return image_path


def detect_emotion(image_path):
    target_emotions = ["happiness", "sadness", "surprise"]
    model = FERModel(target_emotions, verbose=True)
    emotion = model.predict(image_path)
    _write_to_csv(time.strftime("%Y-%m-%d %H:%M:%S"), image_path, emotion)


def webcam_stream_emotion_detection():
    target_emotions = ["happiness", "sadness", "surprise"]
    model = FERModel(target_emotions, verbose=True)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Webcam Stream", frame)
            emotion = model.predict_from_ndarray(frame)
            _write_to_csv(time.strftime("%Y-%m-%d %H:%M:%S"), "webcam_stream", emotion)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cap.release()
    cv2.destroyAllWindows()


def _write_to_csv(timestamp, image_path, emotion):
    with open(CSV_PATH, "a", newline="") as csvfile:
        fieldnames = ["timestamp", "image_path", "emotion"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.stat(CSV_PATH).st_size == 0:
            writer.writeheader()

        writer.writerow(
            {"timestamp": timestamp, "image_path": image_path, "emotion": emotion}
        )
