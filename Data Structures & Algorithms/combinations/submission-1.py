class Solution:

    def helper(self, i, n, k, currset, finalset):
        
        if len(currset) == k:
            finalset.append(currset.copy())
            return
        if i > n:
            return

        
        currset.append(i)
        self.helper(i+1, n, k, currset, finalset)
        currset.pop()
        self.helper(i+1, n, k, currset, finalset)
            

    def combine(self, n: int, k: int) -> List[List[int]]:
        finalset = []
        self.helper(1, n, k, [], finalset)
        return finalset
        