class ChangeDetector:
    def compare(self, prev, curr):
        if prev is None:
            return False, None

        if len(prev) != len(curr):
            return True, None

        for p, c in zip(prev, curr):
            if abs(p['xmin'] - c['xmin']) > 40:
                return True, None

        return False, None
