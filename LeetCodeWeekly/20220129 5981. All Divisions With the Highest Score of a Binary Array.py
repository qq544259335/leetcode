class Solution:
    def maxScoreIndices(self, nums: [int]) -> [int]:
        res = []
        max_calc = 0
        nums_count_right = [0, 0]
        for n in nums:
            nums_count_right[n] += 1
        nums_count_left = [0, 0]

        def calculate(i):
            calc = nums_count_left[0] + nums_count_right[1]
            print(i, calc)
            print(nums_count_left, nums_count_right)
            nonlocal max_calc
            if calc > max_calc:
                max_calc = calc
                res.clear()
                res.append(i)
            elif calc == max_calc:
                res.append(i)

        calculate(0)
        for i in range(len(nums)):
            new_left = nums[i]
            nums_count_left[new_left] += 1
            nums_count_right[new_left] -= 1
            calculate(i + 1)
        return res


test = Solution()
nums = [0, 0, 1, 0]
print(test.maxScoreIndices(nums))
