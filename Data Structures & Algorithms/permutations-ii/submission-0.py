class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in range(0, len(nums)):
            temp_perms = []
            for p in permutations:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, nums[n])
                    if p_copy not in temp_perms:
                        temp_perms.append(p_copy)
            permutations = temp_perms

        return permutations
        