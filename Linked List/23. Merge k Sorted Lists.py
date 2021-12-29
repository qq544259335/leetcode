# Definition for singly-linked list.
import heapq
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        heap = []
        dict = defaultdict(list)
        heapq.heapify(heap)
        head = ListNode(-1)
        cur = head
        for l in lists:
            if l:
                heapq.heappush(heap, l.val)
                dict[l.val].append(l)
        while heap:
            val = heapq.heappop(heap)
            node = dict[val].pop(0)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, node.next.val)
                dict[node.next.val].append(node.next)
        return head.next
