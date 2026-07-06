class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        l_max, r_max = height[l], height[r]
        res = 0

        while l < r:
            
            if height[l] <= height[r]:
                water = min(l_max, r_max) - height[l]
                l += 1
            else:
                water = min(l_max, r_max) - height[r]
                r -= 1

            if water > 0:
                res += water
                
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

        return res
