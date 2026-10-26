class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            currentNumber, left, right = nums[i], i+1, len(nums)-1
            if i > 0 and currentNumber == nums[i-1]:
                continue
            
            while left < right:
                threeSum = currentNumber + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                elif threeSum == 0:
                    res.append([currentNumber, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res