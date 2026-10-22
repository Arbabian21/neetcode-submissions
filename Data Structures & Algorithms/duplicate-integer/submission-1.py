class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        return False if len(numsSet) == len(nums) else True