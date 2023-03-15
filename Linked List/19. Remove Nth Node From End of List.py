# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        fast, slow = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return dummy.next


node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)

solution = Solution()
solution.printer(solution.removeNthFromEnd(node_1, 1))
node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)
solution.printer(solution.removeNthFromEnd(node_1, 2))
node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)
solution.printer(solution.removeNthFromEnd(node_1, 4))
node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)
solution.printer(solution.removeNthFromEnd(node_4, 1))