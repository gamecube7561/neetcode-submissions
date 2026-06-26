class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1
        l_sum = 0
        r_sum = 0

        for num in nums:
            r_sum += num

        for i, num in enumerate(nums):
        
            r_sum -= num
            
            if r_sum == l_sum:
                return i
                
            l_sum += num

        return -1