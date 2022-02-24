# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: [ListNode]) -> [ListNode]:
        cur = head
        nextn = cur.next
        while nextn:
            sum_n = 0
            while nextn.val != 0:
                sum_n += nextn.val
                nextn = nextn.next
            sum_node  = ListNode(sum_n, nextn)
            cur.next = sum_node
            cur = nextn
            nextn = nextn.next
        cur = head.next
        nextn = cur.next
        nextnext = nextn.next
        while nextnext:
            cur.next = nextnext
            cur = nextnext
            nextnext = cur.next.next
        cur.next = None
        return head.next