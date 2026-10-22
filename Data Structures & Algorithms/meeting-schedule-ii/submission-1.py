"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        maxCounter = counter = 0
        s = e = 0
        while s < len(start):
            if start[s] < end[e]: 
                counter += 1
                s+= 1
            else:
                counter -= 1
                e += 1
            maxCounter = max(counter,maxCounter)

        return maxCounter

