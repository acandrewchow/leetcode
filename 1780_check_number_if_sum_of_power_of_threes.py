class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if (n % 3 == 2):  # If there's a '2' in the base-3 representation, return False
                return False
            n //= 3  # Move to the next power of three
        return True  # If no '2' was found, return True