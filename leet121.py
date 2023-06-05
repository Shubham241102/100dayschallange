class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        for x in range (len(prices)):
            for y in range(x+1 , len(prices)):
                if prices[x]< prices[y]:
                    profit = max(profit , prices[y]-prices[x])
                else:
                    break
        return profit
