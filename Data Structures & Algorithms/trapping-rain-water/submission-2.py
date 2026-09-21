class Solution:
    def trap(self, height: list[int]) -> int:

        # Two pointer solution, which is much more intuitive after trying with a stack
        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        res = 0

        # Move the two pointers until they intersect
        while l < r:
            # Since we calculate max_l and max_r at the end of each loop, we will never get a negative diff
            # Move pointer according to the smaller of the values
            if height[l] < height[r]:
                res += min(max_l, max_r) - height[l]
                l += 1
            else:
                res += min(max_l, max_r) - height[r]
                r -= 1

            # Calc new max_l and max_r
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])

        return res
