class Solution:
    
    def helper(self, i, nums, currset, finalset):
        if i >= len(nums):
            finalset.append(currset.copy())
            return
        
        currset.append(nums[i])
        self.helper(i+1, nums, currset, finalset)
        currset.pop()
        self.helper(i+1, nums, currset, finalset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        finalset = []
        self.helper(0, nums, [], finalset)
        return finalset