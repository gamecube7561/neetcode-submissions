class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Answer modeled after the dfs solution.
        We have to go backwards when comparing the two strings, so need a col of 1 values
        """
        
        dp = []
        
        for i in range(len(t)):
            row = [0] * (len(s) + 1)
            dp.append(row)
        dp.append([1] * (len(s) + 1))

        for i in range(len(t) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                if s[j] == t[i]:
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
        
        return dp[0][0]
