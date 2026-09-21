class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        res = []

        # Compares interval 2 start time to interval 1 end time
        def check_int(l1: list[int], l2: list[int]):
            if (l2[0] <= l1[1]):
                return False
            return True

        # Sort the intervals array first so we only need to check the start time
        intervals = sorted(intervals, key = lambda k: k[0])

        for i in range(len(intervals)):
            if res and not check_int(res[-1], intervals[i]):
                i1 = res.pop()
                i2 = intervals[i]
                max_l = min(i1[0], i2[0])
                max_r = max(i1[1], i2[1])
                res.append([max_l, max_r])
            else:
                res.append(intervals[i])

        return res