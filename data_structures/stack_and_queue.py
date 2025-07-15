# stack_and_queue.py
# Simple implementation of stack and queue using lists and deque

from collections import deque

# Stack (LIFO) using list
stack = []

# Adding items (push)
stack.append("a")
stack.append("b")
stack.append("c")
print("Stack:", stack)

# Removing items (pop)
print("Popped:", stack.pop())  # c
print("Stack after pop:", stack)

# Queue (FIFO) using deque
queue = deque()

# Adding items (enqueue)
queue.append("x")
queue.append("y")
queue.append("z")
print("Queue:", queue)

# Removing items (dequeue)
print("Dequeued:", queue.popleft())  # x
print("Queue after dequeue:", queue)
