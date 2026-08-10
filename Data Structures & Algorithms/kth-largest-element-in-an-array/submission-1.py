class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, num)
      
        for i in range(len(h) - k):
            heapq.heappop(h)
        return heapq.heappop(h)
        