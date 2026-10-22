class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        left = 0
        for offset in range((len(nums)-k)+1):
            window = sorted(nums[left+offset:k+offset])
            res.append(window[k-1])

        return res