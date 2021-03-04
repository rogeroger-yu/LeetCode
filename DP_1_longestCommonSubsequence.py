class Solution:
    def longestCommonSubsequence(self, text1, text2):
        text1_len = len(text1)
        text2_len = len(text2)
        dp = [[0 for _ in range(text2_len+1)] for _ in range(text1_len+1)]
        for i in range(1, text1_len+1):
            for j in range(1, text2_len+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
