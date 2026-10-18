class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxp = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxp = max(maxp,prices[sell] - prices[buy])
            elif prices[sell] < prices[buy]:
                buy = sell
                
            sell+=1


        return maxp

            
            
        
        

            