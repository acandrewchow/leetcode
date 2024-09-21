class MyQueue:

    def __init__(self):
        # Two stacks to maintain queue-like
        self.stack1 = []  # Stack for pushing new elements
        self.stack2 = []  # Stack for popping/peeking elements

    def push(self, x: int) -> None:
        # Push element to the back of the queue (which is stack1)
        self.stack1.append(x)

    def pop(self) -> int:
        # Pop element from the front of the queue
        # First, move elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        # Peek at the front element of the queue
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        # Return True if both stacks are empty, False otherwise
        return not self.stack1 and not self.stack2