class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        r = int((len(nums) / 2)*(len(nums)+1))

        for i, num in enumerate(nums):
            total += num

        return r - total