class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([timestamp,value])
        else:
            self.timeMap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        l, r = 0, len(self.timeMap[key]) - 1
        prev = ""

        while l <= r:
            mid = (l+r) // 2
            if self.timeMap[key][mid][0] == timestamp:
                return self.timeMap[key][mid][1]
            elif self.timeMap[key][mid][0] < timestamp:
                prev = self.timeMap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return prev
