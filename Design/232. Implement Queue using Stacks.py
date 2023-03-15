class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


class MyQueue:

    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def push(self, x: int) -> None:
        self.input.push(x)

    def pop(self) -> int:
        if self.output.is_empty():
            for _ in range(self.input.size()):
                self.output.push(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        if self.output.is_empty():
            for _ in range(self.input.size()):
                self.output.push(self.input.pop())
        return self.output.peek()

    def empty(self) -> bool:
        return self.output.is_empty() and self.input.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
