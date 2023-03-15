class Solution:
    def kthPalindrome(self, queries: [int], intLength: int) -> [int]:
        real_length = (intLength + 1) // 2
        max_query = int("9" * real_length) - int("1" + "0" * (real_length - 1)) + 1
        query_one = int("1" + "0" * (real_length - 1))
        res = []
        for q in queries:
            if q > max_query:
                res.append(-1)
                continue
            cur_query = query_one + q - 1
            cur_query = str(cur_query)
            cur_query = cur_query + cur_query[::-1]
            if intLength % 2 == 1:
                cur_query = list(cur_query)
                cur_query.pop(len(cur_query) // 2)
            res.append(int("".join(cur_query)))
        return res
