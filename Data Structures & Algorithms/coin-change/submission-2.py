class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        
        dp.append([0] * (amount + 1))
        
        for j in range(1,len(dp[0])):
            min_coin = float('inf')
            for c in coins:
                if j - c >= 0:
                    min_coin = min(min_coin, dp[-1][j-c] + 1)
            dp[0][j] = min_coin

        
        if dp[-1][-1] == float('inf'):
            return -1

        return dp[-1][-1]