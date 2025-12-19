import math

class ChangeDetector:
    def __init__(self):
        self.prev_objects = []

    def center(self, obj):
        return (
            (obj["xmin"] + obj["xmax"]) / 2,
            (obj["ymin"] + obj["ymax"]) / 2
        )

    def distance(self, a, b):
        ax, ay = self.center(a)
        bx, by = self.center(b)
        return math.sqrt((ax - bx)**2 + (ay - by)**2)

    def detect_changes(self, objects):
        added = []
        deleted = []
        moved = []

        if not self.prev_objects:
            self.prev_objects = objects
            return [], [], []

        # 추가 / 이동 감지
        for obj in objects:
            same_class_prev = [p for p in self.prev_objects if p["class"] == obj["class"]]

            if not same_class_prev:
                added.append(obj)
                continue

            # 가장 가까운 이전 객체와 비교
            min_dist = min(self.distance(obj, p) for p in same_class_prev)
            if min_dist > 50:
                moved.append(obj)

        # 삭제 감지
        for prev in self.prev_objects:
            same_class_now = [o for o in objects if o["class"] == prev["class"]]
            if not same_class_now:
                deleted.append(prev)

        self.prev_objects = objects
        return added, deleted, moved
