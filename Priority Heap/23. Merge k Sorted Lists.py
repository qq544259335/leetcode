# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        # Nlogk k
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        dummy = ListNode(-1)
        p = dummy
        while heap:
            _, index = heapq.heappop(heap)
            p.next = lists[index]
            if lists[index].next:
                heapq.heappush(heap, (lists[index].next.val, index))
            p = p.next
            lists[index] = lists[index].next
        p.next = None
        return dummy.next if dummy.next else None
