class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        elif len(nums) == 1:
            return nums[0]
        
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

            
        