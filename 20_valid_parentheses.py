class Solution:
    def validParentheses(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
    
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Valid parentheses
    s1 = "()[]{}"
    result1 = sol.validParentheses(s1)
    print(f"Test case 1: {s1} is valid: {result1}")  # Expected Output: True

    # Test case 2: Invalid parentheses
    s2 = "(]"
    result2 = sol.validParentheses(s2)
    print(f"Test case 2: {s2} is valid: {result2}")  # Expected Output: False

    # Test case 3: Valid nested parentheses
    s3 = "({[]})"
    result3 = sol.validParentheses(s3)
    print(f"Test case 3: {s3} is valid: {result3}")  # Expected Output: True

    # Test case 4: Empty string (considered valid)
    s4 = ""
    result4 = sol.validParentheses(s4)
    print(f"Test case 4: {s4} is valid: {result4}")  # Expected Output: True

    # Test case 5: Unbalanced parentheses
    s5 = "([)]"
    result5 = sol.validParentheses(s5)
    print(f"Test case 5: {s5} is valid: {result5}")  # Expected Output: False