class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuyinForIndex = [0] * len(prices)
        
        for i in range(len(prices)):
            if i == 0:
                minBuyinForIndex[i] = prices[i]
            else:
                minBuyinForIndex[i] = min(minBuyinForIndex[i-1], prices[i])
            
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - minBuyinForIndex[i])
            
        return maxProfit