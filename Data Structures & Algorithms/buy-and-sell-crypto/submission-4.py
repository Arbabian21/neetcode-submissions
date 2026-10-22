class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, buy, sell = 0, 0, 1

        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, currentProfit)

            if prices[sell] <= prices[buy]:
                buy = sell
            sell += 1
            
        return maxProfit