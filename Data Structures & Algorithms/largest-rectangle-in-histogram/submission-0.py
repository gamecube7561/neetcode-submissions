class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        if not heights:
            return 0

        for num in heights:
            if stack:
                temp = []
                while len(stack) > 0 and stack[-1] > num:
                    temp.append(num)
                    stack.pop()
                if temp:
                    stack += temp
            stack.append(num)
        
            for i, n in enumerate(stack):
                res = max(res, (len(stack) - i) * n)
        
        return res
        