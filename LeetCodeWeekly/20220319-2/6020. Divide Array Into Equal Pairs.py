class Solution:
    def divideArray(self, nums: [int]) -> bool:
        count_dict = {}
        for n in nums:
            if n not in count_dict:
                count_dict[n] = 0
            count_dict[n] += 1
        for k,v in count_dict.items():
            if v % 2 == 1:
                return False
        return True