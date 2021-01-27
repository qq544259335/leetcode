class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, G: list[int]) -> int:
        count = 0
        interal_count = 0
        while head:
            if head.val in G:
                interal_count += 1
            else:
                if interal_count >= 1:
                    count += 1
                interal_count = 0
            head = head.next
        return count 



