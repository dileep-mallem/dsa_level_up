from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)      # add to back   O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()  # remove from front O(1)

    def front(self):
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"front → {list(self._data)} ← back"

# Simulate a printer queue
printer = Queue()
printer.enqueue("doc1.pdf")
printer.enqueue("report.docx")
printer.enqueue("photo.png")

while not printer.is_empty():
    job = printer.dequeue()
    print(f"Printing: {job}")
# Printing: doc1.pdf
# Printing: report.docx
# Printing: photo.png

print()
print("-------------")
print()

q = deque()

# ── Enqueue (add to right/back) ────────────────────────────────
q.append("Alice")
q.append("Bob")
q.append("Priya")
print(q)             # deque(['Alice', 'Bob', 'Priya'])

# ── Peek at front ────────────────────────────────────────────
print(q[0])          # 'Alice'

# ── Dequeue (remove from left/front) — O(1) ─────────────────
first = q.popleft()
print(first)         # 'Alice'
print(q)             # deque(['Bob', 'Priya'])

# ── Check empty ──────────────────────────────────────────────
print(len(q) == 0)   # False

# ── deque also supports appendleft / pop (it's double-ended!) ─
q.appendleft("Zara")  # add to front
q.pop()