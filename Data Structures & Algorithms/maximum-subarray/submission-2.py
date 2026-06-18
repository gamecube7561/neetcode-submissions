class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_l, max_r = 0,0
        max_sub = nums[0]
        cur_sub = 0
        l = 0
        r = 0

        for r in range(len(nums)):
            if cur_sub < 0:
                l = r
                cur_sub = 0

            cur_sub += nums[r]
                
            if cur_sub > max_sub:
                max_sub = cur_sub
        
        return max_sub