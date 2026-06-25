class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = 0
        nums = sorted(nums)
        for num in nums:
            target += num
        target = target / 2

        if target != int(target):
            return False

        dp = []
        for i in range(len(nums) + 1):
            row = [0] * (int(target) + 1)
            dp.append(row)

        for i in range(1, len(nums)+1):
            for j in range(1, int(target)+1):
                include = 0
                if j - nums[i-1] >= 0:
                    include = nums[i-1] + dp[i-1][j-nums[i-1]]
                else:
                    include = dp[i-1][j]
                if include == target:
                    return True
                if not include > target:
                    dp[i][j] = include


        return False
