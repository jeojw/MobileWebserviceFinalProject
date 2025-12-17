import torch

class YoloDetector:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def detect(self, frame):
        results = self.model(frame)
        return results.pandas().xyxy[0].to_dict(orient="records")