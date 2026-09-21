class Solution:
    def trap(self, height: list[int]) -> int:
        # Stack solution, much slower than two pointer   
        max_height = height[0]
        stack = [height[0]]
        res = 0

        for i in range(1, len(height)):
            elm = height[i]
            # If we encounter a new largest value, we pop from the stack and add back the diff
            if stack and elm > stack[0]:
                while stack and elm > stack[0]:
                    popped = heapq.heappop(stack)

                    # As we pop, add the difference to our total
                    diff = min(max_height, elm) - popped
                    res += diff
                    if diff != 0:
                        # Add the popped value back to the stack, but raising the value with the diff
                        heapq.heappush(stack, popped + diff)

            # Add the current elm to the stack and calc new max_height
            heapq.heappush(stack, elm)
            max_height = max(max_height, elm)

        return res