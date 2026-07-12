class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        
        prefix[0] = 1
        suffix[-1] = 1

        res = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[len(nums)-i-1] = nums[len(nums)-i] * suffix[len(nums)-i]
        
        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]
        return res