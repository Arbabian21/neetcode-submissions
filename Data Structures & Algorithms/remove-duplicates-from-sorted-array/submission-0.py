class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        valid = 0
        for invalid in range(len(nums)):
            if nums[valid] != nums[invalid]:
                valid += 1
                nums[valid] = nums[invalid]

        return valid+1