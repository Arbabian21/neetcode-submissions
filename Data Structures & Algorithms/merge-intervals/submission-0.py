class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda i : i[0])
        output = [intervals[0]]
        for currStart, currEnd in intervals[1:]:
            previousEnd = output[-1][1]

            if currStart <= previousEnd:
                output[-1][1] = max(previousEnd, currEnd)
            else:
                output.append([currStart, currEnd])

        return output