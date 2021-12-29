# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        s = None
        f = head
        while f:
            temp = f.next
            f.next = s
            s = f
            f = temp
        return s

    def reverListRecursion(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverListRecursion(head.next)
        head.next.next = head
        head.next = None
        return last

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
sol = Solution()
sol.reverseList(node1)