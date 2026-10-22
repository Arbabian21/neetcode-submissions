class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # handles the edge case of if there's no valid subarray, just return the max value
        currMin, currMax = 1,1
        
        for n in nums:
            temp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            res = max(res, currMax)
        return res