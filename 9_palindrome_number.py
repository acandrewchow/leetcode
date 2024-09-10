class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            # receive our largest divisor
            div = div * 10
            print("Div: ", div)
        
        while x: 
            # extract right digit
            right = x % 10
            # extract left digit
            left = x // div
            print("Right: ", right)
            print("Left: ", left)
            
            if left != right:
                return False
            # chop off left and right digit
            # print("X is:", x)
            x = (x % div) // 10
            # print("X After is:", x)
            # update the value by chopping off 2 digits (100)
            div = div // 100
        return True