class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr = 0
        for sell in range(1,len(prices)):
                
                profit =  prices[sell]-prices[sell-1] 
                curr = max(0,curr+profit)
                max_profit = max(curr,max_profit)
        return max_profit  