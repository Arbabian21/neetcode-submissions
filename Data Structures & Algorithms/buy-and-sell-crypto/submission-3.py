class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, buy, sell = 0, 0, 1

        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, currentProfit)

            if prices[sell] <= prices[buy]:
                if buy +1 == sell:
                    sell += 1
                buy += 1
            elif prices[sell] > prices[buy]:
                sell += 1
            
        return maxProfit