class Solution:
    # o(n)
    def peakIndexInMountainArray(self, arr: [int]) -> int:
        pre = 0
        for i in range(len(arr)):
            if arr[i] < pre:
                return i - 1
            pre = arr[i]

class Solution2:
    # o(log(n))
    def peakIndexInMountainArray(self, arr: [int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = ((l + r) + 1) >> 1
            if arr[mid] - arr[mid - 1] > 0:
                l = mid
            else:
                r = mid - 1
        return l

arr = [0,1,0]
sol = Solution2()
print(sol.peakIndexInMountainArray(arr))