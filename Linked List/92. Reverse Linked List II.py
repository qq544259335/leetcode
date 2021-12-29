class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(-1, head)
        pre, cur= dummy, head
        for i in range(m - 1):
            pre, cur = pre.next, cur.next
        check1, check2 = pre, cur
        pre, cur = pre.next, cur.next
        for i in range(n - 1):
            nextP = cur.next
            cur.next = pre
            pre = cur
            cur = nextP
        check1.next = pre
        check2.next = cur
        return dummy.next

    def reverseBetweenRecursion(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(-1, head)
        cur = dummy
        for i in range(m - 1):
            cur = cur.next

        def recursion(head: ListNode, count: int):
            if count == 0:
                return head, head.next
            last, lastNext = recursion(head.next, count - 1)
            head.next.next = head
            head.next = None
            return last, lastNext

        last, lastNext = recursion(cur.next, n - m)
        cur.next = last
        while cur.next:
            cur = cur.next
        cur.next = lastNext
        return dummy.next

    def reverseBetweenPerfectRecursion(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverseN(head: ListNode, m: int):
            if m == 1:
                return head, head.next
            last ,lastNext = reverseN(head.next, m - 1)
            head.next.next = head
            head.next = lastNext
            return last, lastNext
        if m == 1:
            returnNode, _ = reverseN(head, n)
            return returnNode
        head.next = self.reverseBetweenPerfectRecursion(head.next, m - 1, n - 1)
        return head
