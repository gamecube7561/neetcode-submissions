class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, total = float('-inf'), 0
        r = 0
        while r < len(nums):
            total += nums[r]
            res = max(res, total)
            if total < 0:
                total = 0
            r += 1
        
        return res

        