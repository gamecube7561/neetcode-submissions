class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            num = i
            bits = 0
            while num > 0:
                if num & 1:
                    bits += 1
                num = num >> 1
            res[i] = bits
        return res