class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        seen = {}
        for c in s1:
            count[c] = 1 + count.get(c, 0)
        
        l = 0
        r = 0

        while r < len(s2):
            if count.get(s2[r], None):
                seen[s2[r]] = seen.get(s2[r], 0) + 1
            else:
                length = 0
                seen = {}
                l = r + 1
            while r - l + 1> len(s1):
                seen[s2[l]] = seen.get(s2[l], 1) - 1
                l += 1
            if count == seen:
                return True
            r += 1
            
        return False
        