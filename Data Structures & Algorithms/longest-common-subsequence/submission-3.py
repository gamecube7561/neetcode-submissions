class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = []
        for i in range(len(text1) + 1):
            dp.append([0] * (len(text2) + 1))
        dp2 = dict()
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    max_dp = max(dp[i - 1][j], dp[i][j - 1])
                    dp[i][j] = max_dp
        return dp[-1][-1]
