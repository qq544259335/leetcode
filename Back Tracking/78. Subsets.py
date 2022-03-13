# class Solution:
#     def subsets(self, nums: [int]) -> [[int]]:
#         res = []
#
#         def backtrack(cur, path):
#             if path:
#                 res.append(path[:])
#             if cur == len(nums) - 1:
#                 return
#             for i in range(cur + 1, len(nums)):
#                 path.append(nums[i])
#                 backtrack(i, path)
#                 path.pop(-1)
#
#         backtrack(-1, [])
#         res.append([])
#         return res

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        bitmask = 1 << (len(nums) + 1)
        res = []
        for i in range(bitmask >> 1, bitmask):
            temp = []
            bit_str = bin(i)[2:]
            for i in range(len(bit_str)):
                if bit_str[i] == "1":
                    temp.append(nums[i])
            res.append(temp[:])
        return res
