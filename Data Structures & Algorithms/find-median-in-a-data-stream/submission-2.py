import heapq
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)


    def findMedian(self) -> float:
        self.data.sort()
        if len(self.data) == 0: 
            return 0
        elif len(self.data) == 1: 
            return self.data[0]
        elif len(self.data) %2 != 0: 
            median = len(self.data)//2
            return self.data[median]
        else:
            median1 = len(self.data)//2
            median2 = median1 -1
            actualMedian = (self.data[median1] + self.data[median2])/2
            print(median1,median2)
            print(actualMedian)
            return actualMedian