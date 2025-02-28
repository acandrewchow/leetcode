class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        max_area = 0  

        while l < r:  
            h = min(height[r], height[l])  # Height of the container is the shorter of the two lines
            w = r - l  # Width of the container is the difference between the two pointers
            area = h * w  

            max_area = max(area, max_area)  # Update the maximum area

            # Move the pointer corresponding to the shorter line to try to find a larger area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area  