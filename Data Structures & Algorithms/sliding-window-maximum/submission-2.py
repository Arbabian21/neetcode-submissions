from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        # left = 0
        # for offset in range((len(nums)-k)+1):
        #     window = sorted(nums[left+offset:k+offset])
        #     res.append(window[k-1])
        queue = deque() # contains indecies
        left, right = 0, 0

        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove left val from window
            if left > queue[0]:
                queue.popleft()

            if (right+1) >= k:
                res.append(nums[queue[0]])
                left += 1
            right += 1


        return res