# https://atcoder.jp/contests/abc237/tasks/abc237_d
# n = int(input())
# s = input()
# last = 0
# res = ['0']
# for i in range(n):
#     if s[i] == 'L':
#         res.insert(last, str(i + 1))
#     else:
#         res.insert(last + 1, str(i + 1))
#         last += 1
# print(' '.join(res))

# insert 不是 O(1)所以不是O(n)，要双向链表

class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

dummy = Node(-1, None, None)
n = int(input())
s = input()

new_node = Node('0', dummy, None)
dummy.next = new_node
head = new_node
dummy2 = Node(-1, new_node, None)
new_node.next = dummy2
for i in range(n):
    if s[i] == 'L':
        new_node = Node(str(i + 1), head.prev, head)
        prev = head.prev
        head.prev, prev.next = new_node, new_node
        head = head.prev

    else:
        new_node = Node(str(i + 1), head, head.next)
        next = head.next
        head.next, next.prev = new_node, new_node
        head = head.next
    temp = dummy
    tempa = []
    while temp:
        tempa.append(head.val)
        temp = temp.next

head = dummy.next
temp = ""
while head != dummy2:
    temp += head.val
    head = head.next
    if head != dummy2:
        temp += " "
print(temp)

