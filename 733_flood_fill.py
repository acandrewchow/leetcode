from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        def dfs(r: int, c: int):
            # Check if the current position is out of bounds or not the original color
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return
            
            # Fill the pixel with the new color
            image[r][c] = color
            
            # Recursively call dfs for the four adjacent pixels
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Start the DFS from the initial pixel
        dfs(sr, sc)
        
        return image