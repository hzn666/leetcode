class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        if not self.data:
            self.data.append(num)
        else:
            left, right = 0, len(self.data) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if self.data[mid] >= num:
                    right = mid - 1
                elif self.data[mid] < num:
                    left = mid + 1
            self.data.insert(left, num)

    def findMedian(self) -> float:
        mid = len(self.data) // 2
        if not len(self.data) % 2:
            return sum(self.data[mid - 1:mid + 1]) / 2
        else:
            return self.data[mid]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
