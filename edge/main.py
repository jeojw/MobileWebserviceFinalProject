import cv2
from detector import YoloDetector
from change_detector import ChangeDetector
from uploader import upload_image

detector = YoloDetector()
change_detector = ChangeDetector()

cap = cv2.VideoCapture(0)
prev_objects = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    objects = detector.detect(frame)
    changed = change_detector.compare(prev_objects, objects)

    if changed:
        filename = "change.jpg"
        cv2.imwrite(filename, frame)
        upload_image(filename)

    prev_objects = objects

    cv2.imshow("SmartDesk Watch", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

