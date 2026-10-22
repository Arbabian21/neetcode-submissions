class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        returnArr = [1]*len(nums)
        for i in range(len(nums)-1):
            prefix = prefix * nums[i]
            returnArr[i+1] = prefix * returnArr[i+1]
        

        postfix = 1
        for i in range(len(nums)-1,0,-1):
            postfix = postfix * nums[i]
            returnArr[i-1] = postfix * returnArr[i-1]
        
        return returnArr
        
        