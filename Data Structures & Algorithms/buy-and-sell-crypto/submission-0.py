class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i =0
        max_price = 0
        for i in range(len(prices)-1):
          j = i+1
          while j<len(prices):
             max_price =max(max_price,prices[j]-prices[i])
             j = j+1
        return max_price