class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        returnArr = [1]*len(nums)
        for i in range(len(nums)):
            returnArr[i] *= prefix
            prefix *= nums[i]
        

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            returnArr[i] *= postfix
            postfix *= nums[i]
        
        return returnArr
        
        