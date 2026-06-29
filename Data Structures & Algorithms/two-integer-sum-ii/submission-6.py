class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            t = target - n
            l = i 
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2

                if numbers[mid] == t:
                    return [min(i, mid) + 1, max(i, mid) + 1]
                elif numbers[mid] > t:
                    r = mid - 1
                elif numbers[mid] < t:
                    l = mid + 1
        return []