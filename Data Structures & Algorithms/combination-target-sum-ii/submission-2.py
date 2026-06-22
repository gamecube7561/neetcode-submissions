class Solution:
    def helper(self, i, currset, finalsets, target, curtotal, cand):

        if curtotal == target:

            finalsets.append(currset.copy())
            return
        if curtotal > target or i == len(cand):
            return
        
        currset.append(cand[i])
        self.helper(i+1, currset, finalsets, target, curtotal + cand[i], cand)
        currset.pop()

        while i + 1 < len(cand) and cand[i] == cand[i+1]:
            i += 1

        self.helper(i+1, currset, finalsets, target, curtotal, cand)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        finalset = []
        self.helper(0, [], finalset, target, 0, candidates)
        return finalset
