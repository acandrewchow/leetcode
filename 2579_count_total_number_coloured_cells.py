class Solution:
    def coloredCells(self, n: int) -> int:
        # n = 1 : 1 square
        # n = 2 : 5 squares
        # n = 3 : 13 squares

        res = 1
        i = 0
        while i < n:
            res = res + (4 * i)
            i += 1
        
        return res
        