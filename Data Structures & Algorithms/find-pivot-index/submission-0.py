class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        piv = 0
        l_sum = 0
        r_sum = 0

        for num in nums:
            r_sum += num

        for i in range(len(nums)):
            r_sum -= nums[i]
            if r_sum == l_sum:
                return i
            l_sum += nums[i]
            
        return -1

            
        