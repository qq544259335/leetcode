for t in range(int(input())):
    length = int(input())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    max_n = max(max(nums1), max(nums2))
    max_n2 = 0
    for i in range(length):
        max_n2 = max(max_n2, min(nums1[i], nums2[i]))
    print(max_n2 * max_n)