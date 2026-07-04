class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False] * len(nums)
        res[0] = True

        for i in range(len(res)):
            if res[i] is True:
                
                for j in range(1,nums[i]+1):
                    if i+j >= len(res):
                        break
                    res[i+j] = True       
        return res[-1]