class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_one = False
        found_zero = False

        for char in s:
            if char == '1':
                if found_zero:  
                    return False
                found_one = True
            elif char == '0':
                found_zero = True

        return True
            