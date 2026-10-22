class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive case

            # def dfs(i):
            #     if i >= n: return i ==n
            #     return dfs(i+1) + dfs(i+2)

            # return dfs(0)

        # DP Top down:

            # cache = [-1] *n
            # def dfs(i):
            #     if i >= n: return i == n
            #     if cache[i] != -1: return cache[i]

            #     cache[i] = dfs(i+1) + dfs(i+2)
            #     return cache[i]

            # return dfs(0)
        
        #DP space optimized:

            one, two = 1,1

            for i in range(n-1):
                one, two = one + two, one
            return one