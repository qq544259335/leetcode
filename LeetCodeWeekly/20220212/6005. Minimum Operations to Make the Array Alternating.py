class Solution:
    def minimumOperations(self, nums: [int]) -> int:
        freq_even = {}
        freq_odd = {}
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[1] != nums[0] else 1
        for i in range(len(nums)):
            if i % 2 == 0:
                if nums[i] not in freq_even:
                    freq_even[nums[i]] = 0
                freq_even[nums[i]] += 1
            else:
                if nums[i] not in freq_odd:
                    freq_odd[nums[i]] = 0
                freq_odd[nums[i]] += 1
        print(freq_even)
        print(freq_odd)
        biggest_even = -1
        sec_big_even = -1
        biggest_odd = -1
        sec_big_odd = -1
        for k, v in freq_even.items():
            big = freq_even[biggest_even] if biggest_even != - 1 else -1
            if v > big:
                biggest_even = k
        for k, v in freq_even.items():
            big = freq_even[sec_big_even] if sec_big_even != - 1 else -1
            if v > big and k != biggest_even:
                sec_big_even = k
        for k, v in freq_odd.items():
            big = freq_odd[biggest_odd] if biggest_odd != - 1 else -1

            if v > big:
                biggest_odd = k
        for k, v in freq_odd.items():
            big = freq_odd[sec_big_odd] if sec_big_odd != - 1 else -1
            if v > big and k != biggest_odd:
                sec_big_odd = k
        print(biggest_even, sec_big_even, biggest_odd, sec_big_odd)
        if biggest_odd != biggest_even:
            return len(nums) - freq_even[biggest_even] - freq_odd[biggest_odd]
        else:
            ress = []
            if sec_big_even == -1 and sec_big_odd == -1:
                max_remain = max(freq_even[biggest_even], freq_odd[biggest_odd])
                ress.append(len(nums) - max_remain)
            if sec_big_even != -1 and sec_big_odd == -1:
                ress.append(len(nums) - freq_even[sec_big_even] - freq_odd[biggest_odd])
            if sec_big_odd != - 1 and sec_big_even == -1:
                ress.append(len(nums) - freq_even[biggest_even] - freq_odd[sec_big_odd])
            if sec_big_odd != -1 and sec_big_even != -1:
                ress.append(len(nums) - freq_even[sec_big_even] - freq_odd[sec_big_odd])
            return min(ress)


test = Solution()
nums = [3, 1, 3, 2, 4, 3]
print(test.minimumOperations(nums))
