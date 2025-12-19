import cv2
from detector import ObjectDetector
from change_detector import ChangeDetector
from sender import Sender
import time

detector = ObjectDetector()
changer = ChangeDetector()
sender = Sender(
    server_url="http://<your-django-server>/upload/",
    api_key="MY_SECRET_KEY"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    objects = detector.detect(frame)
    added, deleted, moved = changer.detect_changes(objects)

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

    cv2.imshow("Edge", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

