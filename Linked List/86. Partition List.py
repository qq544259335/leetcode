# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: [ListNode], x: int) -> [ListNode]:
        if not head:
            return None
        p = head
        dummy = ListNode(0, head)
        pre_p = dummy
        q = dummy

        def move(p, q, pre_p):
            q.next, p.next, pre_p.next = p, q.next, p.next

        while p:
            if p.val < x:
                if q.next != p:
                    move(p, q, pre_p)
                q = q.next
            pre_p = p
            p = p.next
        return dummy.next