class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            temps = []
            for p in permutations:
                for i in range(len(p)+1):
                    t = p[:i] + [n] + p[i:]
                    temps.append(t)
            permutations = temps
        return permutations
                
        