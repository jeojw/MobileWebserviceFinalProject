import torch

class ObjectDetector:
    def __init__(self):
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5s")

    def detect(self, frame):
        results = self.model(frame)
        df = results.pandas().xyxy[0]

        objects = []
        for _, row in df.iterrows():
            objects.append({
                "class": row["name"],
                "xmin": row["xmin"],
                "ymin": row["ymin"],
                "xmax": row["xmax"],
                "ymax": row["ymax"]
            })
        return objects
