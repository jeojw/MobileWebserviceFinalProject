class ChangeDetector:
    def compare(self, prev, curr):
        """
        prev, curr: YOLO detection result list
        """
        if prev is None:
            return False

        # 객체 개수 변화
        if len(prev) != len(curr):
            return True

        for p, c in zip(prev, curr):
            # 같은 클래스인지 확인
            if p['name'] != c['name']:
                return True

            # 위치 변화 감지
            if abs(p['xmin'] - c['xmin']) > 40 or abs(p['ymin'] - c['ymin']) > 40:
                return True

        return False

