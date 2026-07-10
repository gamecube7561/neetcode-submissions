class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * len(nums)

        if len(nums) == 1:
            return nums[-1]

        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(nums[i] + res[i-2], res[i-1])

        return max(res[-2], res[-1])
        