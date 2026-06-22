class Solution:
    def helper(self, i, nums, curset, finalset, target, curtotal):
        
        if curtotal > target:
            return
        if curtotal == target:
            finalset.append(curset.copy())

        for j in range(i, len(nums)):
            curset.append(nums[j])
            self.helper(j, nums, curset, finalset, target, curtotal + nums[j])
            curset.pop()

        
        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        finalset = []
        nums = sorted(nums)
        
        self.helper(0, nums, [], finalset, target, 0)
        return finalset