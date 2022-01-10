class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_set = set(s1)
        char_dict = {}
        for c in s1:
            if c not in char_dict.keys():
                char_dict[c] = 0
            char_dict[c] -= 1
        left = 0
        right = 0

        def contains_all():
            for k, v in char_dict.items():
                if v < 0:
                    return False
            return True

        while right < len(s2):
            while not contains_all():
                if right >= len(s2):
                    return False
                cur = s2[right]
                right += 1
                if cur in check_set:
                    char_dict[cur] += 1
            while contains_all():
                cur = s2[left]
                left += 1
                if cur in check_set:
                    char_dict[cur] -= 1
            length = right - 1 - left + 1 + 1
            if length == len(s1):
                return True
        return False
