# Most important idea to make it O(1) is to put key-node into hash table instead of key-val
# Because we are using key to find node, not val.
# Like moveToHead, wu must use key to find node in O(1)
class DoubleLinkedList:
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = DoubleLinkedList(0, 0)
        self.tail = DoubleLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.head
        while node:
            print("we get ", node.key)
            node = node.next
        node = self.tail
        while node:
            print("we reverse got", node.key)
            node = node.prev
        if key in self.cache:
            self.moveToHead(key)
            print('get ', self.cache[key].val)
            return self.cache[key].val
        else:
            print('get -1')
            return - 1

    def put(self, key: int, value: int) -> None:
        node = self.head
        while node:
            print("we get ", node.key)
            node = node.next
        node = self.tail
        while node:
            print("we reverse got", node.key)
            node = node.prev
        if key in self.cache:
            self.changeNodeVal(key, value)
            self.moveToHead(key)
        else:
            if len(self.cache) == self.capacity:
                self.deleteLeastFreq()
            self.addToHead(key, value)

    def moveToHead(self, key: int):
        print('move ', key)
        node = self.cache[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        self.linkToHead(node)
        return

    def addToHead(self, key: int, val: int):
        print('add {} {}'.format(key, val))
        newNode = DoubleLinkedList(key, val)
        self.cache[key] = newNode
        self.linkToHead(newNode)
        return

    def linkToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return

    def deleteLeastFreq(self):
        print('len of dict', len(self.cache))
        print('least freq is ', self.tail.prev.key)
        key = self.tail.prev.key
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        print('delete ', key)
        self.cache.pop(key)
        return

    def changeNodeVal(self, key, val):
        node = self.cache[key]
        node.val = val

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
