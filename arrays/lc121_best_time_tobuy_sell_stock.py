# Learn How to Do problem in Simple and Imrove Obeservations

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if  n<=1 :
            return 0
    
        min_price = prices[0]
        max_profit = 0

        for i in range(1, n):
            price = prices[i]
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price

        return max_profit