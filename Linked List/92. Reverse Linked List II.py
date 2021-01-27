class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre = dummy
        cur = head
        for i in range(m - 1):
            pre = pre.next
            cur = cur.next
        start = pre
        pre = pre.next
        cur = cur.next
        for i in range(n - m):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        start.next.next = cur
        start.next = pre
        return dummy.next