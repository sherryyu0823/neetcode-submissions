class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for i in range(len(prices)):
            if prices[i]<prices[l]:
                l = i
            maxP = max(prices[i]-prices[l], maxP)
        
        return maxP

        

        
        