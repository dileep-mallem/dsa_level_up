class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek on empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Stack{self._data} ← top"

# Demo
s = Stack()
s.push("a"); s.push("b"); s.push("c")
print(s)              # Stack['a', 'b', 'c'] ← top
print(s.peek())       # c
print(s.pop())        # c
print(s.size())       # 2