class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            middle = (left + right)//2
            res = min(res, nums[middle]) 
            if nums[middle] >= nums[left]:
                left = middle +1
            else:
                right = middle -1
        return res
    # [4,5,6,7]
    # left = 0, right = 3
        # middle = 1
            # left = 1
        # res = 5
    # left = 1, right = 3
        # middle = 2
            # left = 2
        # res = 5
    # left = 0, right = 1
        # middle = 0
            # right = 
        # res = 0
        