import math

class ChangeDetector:
    def __init__(self):
        self.prev_objects = []

    def distance(self, a, b):
        ax = (a["xmin"] + a["xmax"]) / 2
        ay = (a["ymin"] + a["ymax"]) / 2
        bx = (b["xmin"] + b["xmax"]) / 2
        by = (b["ymin"] + b["ymax"]) / 2
        return math.sqrt((ax - bx)**2 + (ay - by)**2)

    def detect_changes(self, objects):
        added = []
        deleted = []
        moved = []

        # 이전 객체가 없으면 저장만
        if not self.prev_objects:
            self.prev_objects = objects
            return [], [], []

        # 클래스 기준 매칭
        for obj in objects:
            same_class = [p for p in self.prev_objects if p["class"] == obj["class"]]
            if not same_class:
                added.append(obj)
                continue

            # 거리 기반 동일 객체 여부 확인
            min_dist = min([self.distance(obj, p) for p in same_class])
            if min_dist > 50:  # threshold
                moved.append(obj)

        # 삭제된 객체
        for prev in self.prev_objects:
            same_class = [o for o in objects if o["class"] == prev["class"]]
            if not same_class:
                deleted.append(prev)

        self.prev_objects = objects
        return added, deleted, moved