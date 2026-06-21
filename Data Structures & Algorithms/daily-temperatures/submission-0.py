class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq = deque()
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(dq) > 0 and dq[-1][1] < t:
                ind, temp = dq.pop()
                res[ind] = i - ind
            dq.append((i, t))
        return res
            


            
        