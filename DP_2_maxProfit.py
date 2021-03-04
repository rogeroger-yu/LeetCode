class Solution:
    def maxProfit(self, prices):
        cost = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(price, min_price)
            cost = max(cost, price - min_price)
        return cost
