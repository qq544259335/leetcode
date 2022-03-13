import math


class Solution:
    def replaceNonCoprimes(self, nums: [int]) -> [int]:
        i = 0
        if len(nums) == 1:
            return nums
        while i < len(nums) - 1:
            print('start ', nums)
            print('start i ', i)
            print((math.gcd(nums[i], nums[i + 1])))
            while math.gcd(nums[i], nums[i + 1]) == 1:
                print('gcd ', nums[i], " ", nums[i + 1])
                i += 1
                if i == len(nums) - 1:
                    return nums
            print('not gcd ', nums[i], " ", nums[i + 1])
            temp = nums[i] * nums[i + 1] // math.gcd(nums[i], nums[i + 1])
            nums.pop(i)
            nums[i] = temp
            i -= 1
            i = i if i >= 0 else 0
            print("after update ", nums)
            if len(nums) == 1:
                return nums
