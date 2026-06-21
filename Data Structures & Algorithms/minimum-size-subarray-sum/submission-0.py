class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        temp_target = 0
        l, r = 0, 0
        while r < len(nums):
            temp_target += nums[r]
            
            if temp_target >= target:
                while temp_target >= target:
                    min_size = min(min_size, r - l + 1)
                    temp_target -= nums[l]
                    l += 1
            
            r += 1
        if min_size == float('inf'):
            return 0
        return min_size