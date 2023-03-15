class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        i = 0
        j = len(arr) - k
        while i <= j:
            mid = i + (j - i) // 2
            if mid + k == len(arr):
                return arr[mid:mid+k]
            if abs(x - arr[mid]) <= abs(arr[mid + k] - x): # move left for same abs but smaller num 5 6 6 7
                if arr[mid] != arr[mid + k]: # move rightmost for a series of identical nums 2 2 2 2 2 2 2
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                i = mid + 1
        return arr[i:i + k]
    def findClosestElementsSlidingWindow(self, arr: [int], k: int, x: int) -> [int]:
        i , j = 0, len(arr) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if x <= arr[mid]:
                j = mid - 1
            else:
                i = mid + 1

        left = i - 1 if i != len(arr) else len(arr) - 1
        right = left + 1
        print(left, right)
        while right - 1 - (left + 1) + 1 < k:
            if left == -1:
                right += 1
            elif right == len(arr):
                left -= 1
            else:
                if abs(x- arr[right]) < abs(x - arr[left]):
                    right += 1
                else:
                    left -= 1
        return arr[left + 1: right]

sol = Solution()
sol.findClosestElementsSlidingWindow([1, 1, 2, 2, 2, 2, 2, 3, 3], 3, 3)
