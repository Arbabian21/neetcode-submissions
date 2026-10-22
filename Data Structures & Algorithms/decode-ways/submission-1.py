class Solution:
    def numDecodings(self, s: str) -> int:
        #dp recursions
            # cache = {len(s): 1}

            # def dfs(i):
            #     if i in cache: return cache[i]
            #     if s[i] == "0": return 0

            #     res = dfs(i+1)

            #     if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
            #         res += dfs(i+2)
                
            #     cache[i] = res
            #     return res

            # return dfs(0)
        
        # dp linear
            cache = {len(s): 1}

            for i in range(len(s)-1,-1,-1):
                if s[i] == "0": 
                    cache[i] = 0
                else:
                    cache[i] = cache[i+1]

                if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                    cache[i] += cache[i+2]

            return cache[0]