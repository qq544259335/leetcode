# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        firstP = head
        for _ in range(n):
            firstP = firstP.next
        secondP = head
        if not firstP:
            return head.next
        while firstP.next:
            firstP = firstP.next
            secondP = secondP.next
        secondP.next = secondP.next.next
        return head