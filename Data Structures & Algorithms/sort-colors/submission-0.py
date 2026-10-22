class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        frequency = [0] * 3

        for currNum in nums:
            frequency[currNum] += 1
        
        k = 0
        for i in range(len(frequency)):
            for j in range(frequency[i]):
                nums[k] = i
                k += 1

        return nums

