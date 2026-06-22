class Solution:
    def helper(self, i, currset, finalset, n, k):
        
        if len(currset) == k:
            finalset.append(currset.copy())
            return
        if i > n:
            return

        currset.append(i)

        self.helper(i + 1, currset, finalset, n, k)

        currset.pop()

        self.helper(i + 1, currset, finalset, n, k)
        

    def combine(self, n: int, k: int) -> List[List[int]]:
        finalset =  []
        self.helper(1, [], finalset, n ,k)
        return finalset