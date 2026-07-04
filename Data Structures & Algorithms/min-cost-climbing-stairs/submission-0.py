class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [cost[0], cost[1]]
        
        for i in range(2, len(cost)+1):
            if i >= len(cost):
                curr_cost = 0
            else:
                curr_cost = cost[i]
            res.append(curr_cost + min(res[i-1], res[i-2]))

        return res[-1]
        