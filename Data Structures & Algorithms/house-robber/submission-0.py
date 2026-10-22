class Solution:
    def rob(self, nums: List[int]) -> int:
        # recursivee:
            # def dfs(i):
            #     if i >= len(nums): return 0
            #     return max(dfs(i+1), nums[i] + dfs(i+2))

            # return dfs(0)
        
        # Dynamic Programming top down:

            # cache = [-1]* len(nums)

            # def dfs(i):
            #     if i >= len(nums): return 0
            #     if cache[i] != -1: return cache[i]

            #     cache[i] = max(dfs(i +1), nums[i] + dfs(i+2))
            #     return cache[i]

            # return dfs(0)

        # DP Space optimized:
            rob1, rob2 = 0, 0

            for value in nums:
                temp = max(value + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
            