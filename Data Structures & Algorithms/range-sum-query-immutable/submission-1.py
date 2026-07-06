class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0

        for i in range(max(0, left), min(len(self.nums), right+1)):
            print(self.nums[i])
            total += self.nums[i]
        
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)