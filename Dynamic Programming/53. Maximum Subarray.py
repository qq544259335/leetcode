class Solution:
        def maxSubArray(self, nums: [int]) -> int:
            sum_all = nums[0]
            res = sum_all
            for i in range(1,len(nums)):
                sum_all = max(sum_all + nums[i], nums[i])
                res = res if sum_all < res else sum_all
            return res

        def maxSubArray2(self, nums: [int]) -> int:  # 分治
            def f(nums, l, r):
                if l == r:
                    return nums[l], nums[l], nums[l], nums[l]
                m = (l + r) // 2
                lsum1, rsum1, sum1, msum1 = f(nums, l, m)
                lsum2, rsum2, sum2, msum2 = f(nums, m + 1, r)
                return max(lsum1, sum1 + lsum2), max(rsum2, sum2 + rsum1), sum1 + sum2, max(msum1, msum2, rsum1 + lsum2)

            a, b, c, res = f(nums, 0, len(nums) - 1)
            return res


solve = Solution()
print(solve.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))