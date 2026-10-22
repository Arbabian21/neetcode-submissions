class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i in range(len(nums)):
            have = nums[i]
            want = target - have
            if want in dictionary.keys():
                return [dictionary[want], i]
            else:
                dictionary[have] = i