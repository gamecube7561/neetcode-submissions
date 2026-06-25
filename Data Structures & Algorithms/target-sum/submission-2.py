class Solution:
    def helper(self, i, nums, total, target, cache):
        if i == len(nums):
            if total == target:
                return 1
            else:
                return 0

        if (i, total) in cache:
            return cache.get((i, total))

        cache[(i, total)] = self.helper(i + 1, nums, total + nums[i], target, cache) + self.helper(i + 1, nums, total - nums[i], target, cache)
        return cache[(i, total)]
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        return self.helper(0, nums, 0, target, cache)