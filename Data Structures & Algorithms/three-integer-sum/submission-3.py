class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        returnArr = []
        for i in range(len(nums)-1):
            currentNum, left, right = nums[i], i+1, len(nums)-1
            if i > 0 and currentNum == nums[i-1]:
                continue
            
            while left < right:
                threeSum = currentNum + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                elif threeSum == 0:
                    returnArr.append([currentNum, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return returnArr
                
