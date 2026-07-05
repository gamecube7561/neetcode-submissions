class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numset = {}
        pairs = 0
        for num in nums:
            if num in numset:
                pairs += numset[num]
                numset[num] += 1
            else:
                numset[num] = 1
        
        return pairs
        