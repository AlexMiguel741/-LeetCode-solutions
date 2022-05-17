# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #if prices.sort(reverse=True)==prices:
        
        minimum_price=99999
        maximum_profit=0
        
        for price in prices:
            minimum_price=min(price, minimum_price)
            
            profit=price-minimum_price
            
            maximum_profit=max(maximum_profit,profit)
            
        return maximum_profit
