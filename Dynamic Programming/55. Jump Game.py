class Solution:
    def canJump(self, nums: [int]) -> bool:
        count = 0
        for i in range(len(nums)):
            count = max(nums[i], count - 1)
            if count == 0 and i != len(nums) - 1:
                return False
        return True

    # canJump2 will break the iteration when rightmost can skip to the end while canJump must iterate whole nums
    def canJump2(self, nums: [int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
            else:
                return False
        return False


sol =Solution()
array = [2,3,1,1,4]
print(sol.canJump(array))