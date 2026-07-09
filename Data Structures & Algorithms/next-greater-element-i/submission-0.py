class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            if num1 not in nums2:
                res.append(-1)
                continue
            idx = 0
            val = -1
            for i in range(len(nums2)):
                if nums2[i] == num1:
                    idx = i
                    break
            for j in range(i, len(nums2)):
                if nums2[j] > num1:
                    val = nums2[j]
                    break
            res.append(val)
        return res