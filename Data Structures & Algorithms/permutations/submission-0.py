class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            temp_perms = []
            for p in permutations:
                for i in range(len(p)+1):
                    temp_p = p.copy()
                    temp_p.insert(i, n)
                    temp_perms.append(temp_p)
            permutations = temp_perms
            
        return permutations