from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Start from the last digit and move left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # If digit is less than 9, just add 1
                return digits    # no carry we can return result
            digits[i] = 0  # If digit is 9 turn it to 0 (carry over)

        # need an extra '1' at the front when loop ends (indicates it ends in 9)
        return [1] + digits