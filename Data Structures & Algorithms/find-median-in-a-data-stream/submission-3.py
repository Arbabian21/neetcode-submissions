class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        if not self.data: return 0
        if len(self.data) == 1: return self.data[0]
        self.data.sort()
        median = len(self.data)//2
        if len(self.data)%2 != 0:
            return self.data[median]
        else:
            return ((self.data[median-1] + self.data[median])/2)