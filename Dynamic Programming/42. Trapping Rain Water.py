class Solution:
    # n**2
    def trap_brute_force(self, height: [int]) -> int:
        res = 0
        for i in range(len(height)):
            max1 = i
            max2 = i
            p1 = i
            p2 = i
            while p1 - 1 >= 0:
                p1 -= 1
                max1 = max1 if height[max1] > height[p1] else p1
            while p2 + 1 < len(height):
                p2 += 1
                max2 = max2 if height[max2] > height[p2] else p2
            if max1 != i and max2 != i:
                res += min(height[max2], height[max1]) - height[i]
        return res

    # 显然brute force的时候后很多重复的左右最大查询，对 i 左最大只能是 0 to i，右最大是 i to n - 1，显然不能用一个变量存储
    # 可以通过左最大右最大分别维护一个队列
    # N N
    def trap_dp(self, height: [int]) -> int:
        l = len(height)
        left_max = [0] * l
        right_max = [0] * l
        res = 0
        left_max[0] = height[0]
        for i in range(1,l):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max[l - 1] = height[l - 1]
        for i in range(l - 2, -1, - 1):
            right_max[i] = max(right_max[i + 1], height[i])
        for i in range(0, l):
            res += min(left_max[i], right_max[i]) - height[i]
        return res

    # https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
    # 双指针，天秀
    # 把问题本质化简，就是对height[i]找到左边右边最大值里比较小的哪个
    # T N S 1
    def trap(self, height: [int]) -> int:
        left_max = 0
        right_max = 0
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                left_max = left_max if left_max >= height[left] else height[left]
                res += left_max - height[left]
                left += 1
            else:
                right_max = right_max if right_max >= height[right] else height[right]
                res += right_max - height[right]
                right -= 1
        return res

sol = Solution()
height = [4, 2, 0, 3, 2, 5]
print(sol.trap_dp(height))
