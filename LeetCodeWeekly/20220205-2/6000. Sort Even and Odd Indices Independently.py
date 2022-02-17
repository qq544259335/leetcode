class Solution:
    def sortEvenOdd(self, nums: [int]) -> [int]:
        evens = []
        odds = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        evens.sort()
        odds.sort()
        odds = odds[::-1]
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(evens[i // 2])
            else:
                res.append(odds[i // 2])

        return res


nums = [36, 45, 32, 31, 15, 41, 9, 46, 36, 6, 15, 16, 33, 26, 27, 31, 44, 34]
test = Solution()
print(test.sortEvenOdd(nums))
