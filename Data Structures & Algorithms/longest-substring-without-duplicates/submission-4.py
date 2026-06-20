class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = deque()
        longest = 0
        temp = 0

        for i in range(0, len(s)):
            c = s[i]

            while c in seen:
                seen.popleft()
                temp -= 1

            temp += 1
            seen.append(c)
            longest = max(longest, temp)
        return longest