class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            midpoint = (left + right) // 2

            if target == nums[midpoint]:
                return midpoint
            if target > nums[midpoint]:
                left = midpoint + 1
            if target < nums[midpoint]:
                right = midpoint - 1

        return -1
            