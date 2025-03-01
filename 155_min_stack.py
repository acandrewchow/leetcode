class MinStack:
    # O(1)
    def __init__(self):
        self.stack = [] # normal stack
        self.min_stack = [] # min stack
        

    def push(self, val: int) -> None:
        self.stack.append(val) # always push to main stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val) # only push to min_stack if new minimum value

        
    def pop(self) -> None:
        if self.stack:
            popped_value = self.stack.pop()
            if popped_value == self.min_stack[-1]:
                self.min_stack.pop() # remove from min_stack if it was the min
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()