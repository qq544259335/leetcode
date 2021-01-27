# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp_head = ListNode(-1, head)
        start = temp_head
        while start is not None:
            ptr = start.next
            while ptr is not None and ptr.next is not None and ptr.val == ptr.next.val:
                ptr = ptr.next
            if ptr is not None and ptr != start.next:
                start.next = ptr.next
                continue
            start = ptr
        return temp_head.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        temp_head = ListNode(-1, head)
        start = temp_head
        ptr = start.next
        while ptr and ptr.next:
            if ptr.next.val != ptr.val:
                start = start.next
                ptr = ptr.next
            else:
                while ptr and ptr.next and ptr.val == ptr.next.val:
                    ptr = ptr.next
                ptr = ptr.next
                start.next = ptr
        return temp_head.next