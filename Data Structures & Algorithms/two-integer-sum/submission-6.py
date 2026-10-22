class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, number in enumerate(nums):
            if (target-number) in seen.keys(): return [seen[target-number], index]
            seen[number] = index
