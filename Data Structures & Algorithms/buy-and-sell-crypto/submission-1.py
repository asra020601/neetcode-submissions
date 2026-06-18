class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            curr = 0
            for j in range(i+1,len(prices)):
                profit =  prices[j]-prices[i] 
                curr = max(curr,profit)
            max_profit = max(curr,max_profit)
        return max_profit  