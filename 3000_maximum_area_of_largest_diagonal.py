class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0

        for l, w in dimensions:
            d = sqrt(l * l + w * w)
          
            a = l * w
            
            if d > max_diagonal or (d == max_diagonal and a > max_area):
                max_diagonal = d
                max_area = a
        
        return max_area
        