import torch

class YoloDetector:
    def __init__(self):
        # YOLOv5s pretrained model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def detect(self, frame):
        results = self.model(frame)
        # pandas DataFrame → dict list
        return results.pandas().xyxy[0].to_dict(orient="records")
