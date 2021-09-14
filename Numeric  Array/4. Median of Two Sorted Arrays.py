class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        def binarSearch(k: int) -> int:
            index1, index2 = 0, 0
            while True:
                if len(nums1) == index1 or len(nums2) == index2:
                    return nums2[index2 + k - 1] if len(nums1) == index1 else nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                newIndex1 = min(index1 + k // 2 - 1, len(nums1) - 1)
                newIndex2 = min(index2 + k // 2 - 1, len(nums2) - 1)
                if nums1[newIndex1] <= nums2[newIndex2]:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        n, m = len(nums1), len(nums2)
        if (n + m) % 2 == 0:
            return (binarSearch((len(nums1) + len(nums2)) // 2) + binarSearch((len(nums1) + len(nums2)) // 2 + 1)) / 2
        else:
            return binarSearch((len(nums1) + len(nums2)) // 2 + 1)


arr1 = [2]
arr2 = [1, 3, 4]
sol = Solution()
print(sol.findMedianSortedArrays(arr1, arr2))
