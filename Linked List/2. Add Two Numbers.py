# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = ListNode(0, None)
        pos = res
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            toAdd = val1 + val2 + carry
            if toAdd <= 9:
                carry = 0
            else:
                carry = 1
                toAdd -= 10
            newNode = ListNode(toAdd, None)
            pos.next = newNode
            pos = pos.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if carry != 0:
            newNode = ListNode(carry, None)
            pos.next = newNode
        return res.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        pos = ListNode(0, l2)
        res = l2
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            toAdd = val1 + val2 + carry
            if toAdd <= 9:
                carry = 0
            else:
                carry = 1
                toAdd -= 10
            if l2:
                l2.val = toAdd
            else:
                newNode = ListNode(toAdd, None)
                pos.next = newNode
            pos = pos.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if carry != 0:
            newNode = ListNode(carry, None)
            pos.next = newNode
        return res


la4 = ListNode(1)
la3 = ListNode(5, la4)
la2 = ListNode(4, la3)
la1 = ListNode(2, la2)
lb3 = ListNode(4)
lb2 = ListNode(6, lb3)
lb1 = ListNode(5, lb2)
sol = Solution()
res = sol.addTwoNumbers2(la1, lb1)
while res:
    print(res.val)
    res = res.next
