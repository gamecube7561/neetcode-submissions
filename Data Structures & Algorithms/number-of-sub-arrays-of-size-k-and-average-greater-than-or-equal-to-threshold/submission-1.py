class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        r = l + k
        total = 0
        for i in range(l, r):
            total += arr[i]

        while r <= len(arr):
            
            
            if (total / k) >= threshold:
                res +=1
            print(l,r, total/ k)

            total -= arr[l]
            if r < len(arr):
                total += arr[r]
            l += 1
            r += 1

            
        # for l in range(len(arr)-k+1):
        #     total = 0
        #     r = l + k
        #     for i in range(l, min(len(arr), l + k)):
        #         total += arr[i]
        #     if total // k > threshold:
        #         res += 1
        return res

        