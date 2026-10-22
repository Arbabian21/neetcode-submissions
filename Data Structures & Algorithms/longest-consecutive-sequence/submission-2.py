class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSequence = 0
        for number in nums:
            currentNumber = number
            if currentNumber-1 not in numSet:
                currentLen = 1
                while currentNumber+1 in numSet:
                    currentLen += 1
                    currentNumber += 1
                maxSequence = max(maxSequence, currentLen)
        
        return maxSequence