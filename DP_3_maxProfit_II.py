class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1:
            return 0
        dp = [[0]*2]*length
        dp[0][0] = 0
        dp[0][1] = prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[length-1][0]
