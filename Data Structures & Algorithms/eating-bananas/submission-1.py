class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best_time = float('inf')
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            time = 0
            
            for p in piles:
                time += math.ceil(p/mid)
            if time <= h:
                best_time = min(best_time, mid)
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
            
        return best_time   