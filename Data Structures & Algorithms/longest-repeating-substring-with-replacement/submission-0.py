class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        characters = {}
        res = 0
        for c in "ACBCDEFGHIJKLMNOPQRSTUVWXYZ":
            characters[c] = 0

        l = r = 0

        while r < len(s):
            characters[s[r]] += 1
            max_freq = max(max_freq, characters[s[r]])

            while (r - l + 1) - max_freq > k:
                characters[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res
