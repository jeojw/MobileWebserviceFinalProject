import cv2
import time
from detector import ObjectDetector
from change_detector import ChangeDetector
from sender import Sender
import os
from config import SERVER_URL, API_KEY

detector = ObjectDetector()
change_detector = ChangeDetector()
sender = Sender(SERVER_URL, API_KEY)

os.makedirs("frames", exist_ok=True)

cap = cv2.VideoCapture(0)  # 웹캠

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    objects = detector.detect(frame)
    added, deleted, moved = change_detector.detect_changes(objects)

    if added or deleted or moved:
        timestamp = int(time.time())
        filename = f"frames/change_{timestamp}.jpg"
        cv2.imwrite(filename, frame)

        if added:
            sender.send(filename, "added")
        if deleted:
            sender.send(filename, "deleted")
        if moved:
            sender.send(filename, "moved")

    cv2.imshow("SmartDesk Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
