class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        seen.append(n)
        total = 0
        
        while True:
            total = 0
            
            for c in str(n):
                total += int(c) ** 2
            
            if total in seen:
                break
            elif total == 1:
                break

            n = total
            seen.append(n)

        return total == 1
