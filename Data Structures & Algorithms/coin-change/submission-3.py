class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP Top down
            # cache = {} # the current amount needed i.e goal is 6, you need amounts 0 - 6
            #         # mapping ammount as index to coins needed to acheive that ammount

            # def dfs(remainder):
            #     if remainder == 0:
            #         return 0
            #     if remainder in cache:
            #         return cache[remainder]

            #     res = float("inf")
            #     for coin in coins:
            #         if remainder - coin >= 0:
            #             res = min(res, 1 + dfs(remainder-coin))
            #     cache[remainder] = res
            #     return res
                
            # minCoins = dfs(amount)
            # return minCoins if minCoins < float("inf") else -1

        # DP Bottom Up
            dp = [float("inf")] * (amount+1) 
            # because you want to cache the number of coins you need for each value from 0 to the target amount
            # float("inf") bc you want to make the default number of coins for each value from 0 to the target 
            # amount infinity bc you want the minimum
            dp[0] = 0 # you only ever need 0 coins to get an ammount of 0

            for currAmount in range(1, amount+1):
            # because this approach is technically brute force you need to calculate every way to get each 
            # amount leading up to the target amount
                for coin in coins: # you're going to check every possible coin for the current ammount
                    if currAmount - coin >= 0:
                    # if it's a valid coin
                        dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - coin])
                        # the min number of coins needed to reach the current amount which is whatever 
                        # amount we're at leading up to target amount, minus the current coin we're at, 
                        # and it's equal to the minimum of whatever is already stored there (so initally 
                        # infinity but bc there are multiple ways to get the current target amount, it's 
                        # going to change with every coin) so the minimum of that or 1 plus the number of 
                        # coins needed for the current amount minus the current coin if it's already cached

            return dp[amount] if dp[amount] != float("inf") else -1
