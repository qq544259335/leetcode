class Solution:
    def sortJumbled(self, mapping: [int], nums: [int]) -> [int]:
        changed_nums = []
        for i in range(len(nums)):
            number = nums[i]
            new_number = 0
            time = 0
            while number != 0:
                new_number += time * mapping[number % 10]
                number //= 10
                time += 1
            changed_nums.append((new_number, i))
        changed_nums.sort(key=lambda x: (x[0], x[1]))
        res = []
        for i in range(len(changed_nums)):
            res.append(nums[changed_nums[i][1]])
        return res
