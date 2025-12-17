import cv2
from detector import YoloDetector
from change_detector import ChangeDetector
from uploader import upload_image
import time

detector = YoloDetector()
change_detector = ChangeDetector()
cap = cv2.VideoCapture(0)

prev_objects = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    curr_objects = detector.detect(frame)
    changed, diff = change_detector.compare(prev_objects, curr_objects)

    if changed:
        filename = f"change_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print("🔔 Change detected → uploading...")
        upload_image(filename)

    prev_objects = curr_objects

