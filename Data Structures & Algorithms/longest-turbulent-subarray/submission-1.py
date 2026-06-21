class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res = 1
        up_down = ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and up_down != ">":
                res = max(res, r - l + 1)
                r += 1
                up_down = ">"
            elif arr[r - 1] < arr[r] and up_down != "<":
                res = max(res, r - l + 1)
                r += 1
                up_down = "<"
            else:
                r = r + 1 if arr[r] == arr[r-1] else r
                l = r - 1
                up_down = ""

        return res




        
        