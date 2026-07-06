class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        finalset = []
        nums.sort()

        def helper(i, nums, currset, finalset):
            if i >= len(nums):
                finalset.append(currset.copy())
                return

            currset.append(nums[i])
            helper(i + 1, nums, currset, finalset)
            currset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, nums, currset, finalset)

        helper(0, nums, [], finalset)
        return finalset
