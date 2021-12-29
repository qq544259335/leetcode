class Solution:
    # brute force
    def removeDuplicatesDummy(self, s: str, k: int) -> str:
        pivot = 0
        dup_count = 1
        last = ' '
        last_pivot = 0
        while pivot < len(s):
            print(pivot, dup_count, last, last_pivot)
            if last == s[pivot]:
                dup_count += 1
                pivot += 1
                if dup_count == k:
                    s = s[:last_pivot] + s[pivot:] if pivot < len(s) else s[:last_pivot]
                    print(s)
                    pivot = last_pivot - k if last_pivot - k >= 0 else 0
                    last_pivot = pivot
                    pivot += 1
                    last = s[last_pivot]
                    dup_count = 1
            else:
                last_pivot = pivot
                pivot += 1
                dup_count = 1
                last = s[last_pivot]
        return s

    # add history t 15% O(n) big c; s 15%  O(n) big c
    def removeDuplicatesDummyImprove(self, s: str, k: int) -> str:
        pivot = 0
        dup_count = 1
        last = ' '
        last_pivot = 0
        history_queue = []
        while pivot < len(s):
            print(pivot, dup_count, last, last_pivot)
            if last == s[pivot]:
                dup_count += 1
                pivot += 1
                if dup_count == k:
                    s = s[:last_pivot] + s[pivot:] if pivot < len(s) else s[:last_pivot]
                    print(s)
                    # pivot = last_pivot - k if last_pivot - k >= 0 else 0
                    # last_pivot = pivot
                    # pivot += 1
                    # last = s[last_pivot]
                    # dup_count = 1
                    if history_queue:
                        history = history_queue.pop(-1)
                        last, last_pivot, pivot, dup_count = history
                        pivot += 1
                    else:
                        pivot = 0
                        dup_count = 1
                        last = ' '
                        last_pivot = 0
            else:
                if last != ' ':
                    history_queue.append((last, last_pivot, pivot - 1, dup_count))
                print(history_queue)
                last_pivot = pivot
                pivot += 1
                dup_count = 1
                last = s[last_pivot]
        return s

    def removeDuplicatesSlow(self, s: str, k: int) -> str:
        stack = []
        p = 0
        while p < len(s):
            if p == 0 or s[p] != s[p - 1]:
                stack.append(1)
            else:
                stack[-1] += 1
                if stack[-1] == k:
                    s = s[:p - k + 1] + s[p + 1:] if p + 1 < len(s) else s[:p - k + 1]
                    p -= k
                    stack.pop(-1)
            p += 1
        return s

    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or c != stack[-1][0]:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop(-1)
        return ''.join(c * b for c, b in stack)

sol = Solution()
s = "deeedbbcccbdaa"
k = 3
print(sol.removeDuplicates(s, k))
