class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow, pos = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while pos != slow:
                    slow = slow.next
                    pos = pos.next
                return pos
        return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        nodeSet = set()
        while head:
            if head not in nodeSet:
                nodeSet.add(head)
            else:
                return head
            head = head.next
        return None

    def detectCycle3(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None