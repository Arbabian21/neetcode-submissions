class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        eraseCounter = 0
        intervals.sort(key= lambda i:i[0])
        previousEnd = intervals[0][1]
        for currStart,currEnd in intervals[1:]:
            if currStart < previousEnd:
                eraseCounter += 1
                previousEnd = min(currEnd,previousEnd)
            else:
                previousEnd = currEnd
        return eraseCounter
            
