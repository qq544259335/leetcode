# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoListsIteration(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode()
        pos = prehead
        while l1 and l2:
            if l1.val < l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        pos.next = l1 if l1 else l2
        return prehead.next

    def mergeTwoListsRecursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoListsRecursion(l1.next, l2)
            return l1
        elif l2.val < l1.val:
            l2.next = self.mergeTwoListsRecursion(l1, l2.next)
            return l2
        return None

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        res = dummy
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        res.next = l1 if l1 else l2
        return dummy.next

n3 = ListNode(4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
n6 = ListNode(4)
n5 = ListNode(3, n6)
n4 = ListNode(1, n5)
sol = Solution()
n = sol.mergeTwoListsRecursion(n1, n4)
while n:
    print(n.val)
    n = n.next
