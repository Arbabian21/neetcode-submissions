class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        sequenceLength = 0
        for i in setNums:
            currNum = i
            if currNum-1 not in setNums:
                currSequence = 1
                while currNum+1 in setNums:
                    currNum += 1
                    currSequence += 1
                sequenceLength = max(sequenceLength, currSequence)
        return sequenceLength