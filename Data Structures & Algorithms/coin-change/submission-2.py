class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {} # the current amount needed i.e goal is 6, you need amounts 0 - 6
                   # mapping ammount as index to coins needed to acheive that ammount

        def dfs(remainder):
            if remainder == 0:
                return 0
            if remainder in cache:
                return cache[remainder]

            res = float("inf")
            for coin in coins:
                if remainder - coin >= 0:
                    res = min(res, 1 + dfs(remainder-coin))
            cache[remainder] = res
            return res
            
        minCoins = dfs(amount)
        return minCoins if minCoins < float("inf") else -1