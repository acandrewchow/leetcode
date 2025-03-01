class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # pop 2 at a time and perform the corresponding operation
        # final evaluation is present in the stack
        # we read left -> right
        stack = []

        for token in tokens:
            if token == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(int(a + b))
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))
            
        return stack[0]

        