class Solution:
    def jump(self, nums: [int]) -> int:
        rightmost = 0
        pos = 0
        jump = 0
        while pos != len(nums) - 1:
            step = nums[pos]
            next_pos = 0
            for i in range(1, step + 1):
                if pos + i >= len(nums) - 1:
                    return jump + 1
                if pos + i + nums[pos + i] > rightmost:
                    rightmost = pos + i + nums[pos + i]
                    next_pos = pos + i
            pos = next_pos
            jump += 1
        return jump

    # jump is O(n*n)
    # jumpFaster is O(n)

    def jumpFaster(self, nums: [int]) -> int:
        rightmost, end, jump = 0, 0, 0
        for i in range(len(nums) - 1): # if we take the last index into count, we will get we more wrong jump
            rightmost = max(rightmost, i + nums[i])
            if i == end:
                end = rightmost
                jump += 1
        return jump


sol = Solution()
array = [2, 3, 1, 1, 4]
print(sol.jumpFaster(array))
