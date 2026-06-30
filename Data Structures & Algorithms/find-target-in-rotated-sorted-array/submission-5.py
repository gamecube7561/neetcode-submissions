class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        p = 0

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        p = l

        if target >= nums[p] and target <= nums[len(nums) - 1]:
            l = p
            r = len(nums) - 1
        else:
            l = 0
            r = p - 1

        if nums[0] == target:
            return 0
        elif nums[-1] == target:
            return len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
        