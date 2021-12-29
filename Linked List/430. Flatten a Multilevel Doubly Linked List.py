# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        stack = []
        while cur or stack:
            if not cur.child and cur.next:
                cur = cur.next
            elif cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur = cur.child
            else:
                if not stack:
                    break
                connect_node = stack.pop(-1)
                cur.next = connect_node
                connect_node.prev = cur.next
                cur = cur.next
        return head