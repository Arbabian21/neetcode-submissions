class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[purchase] < prices[sell]:
                profit = (prices[sell] - prices[purchase])
                maxProfit = max(maxProfit, profit)
                
            else:
                purchase = sell

            sell += 1

        return maxProfit