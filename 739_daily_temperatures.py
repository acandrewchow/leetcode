from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        # Stack to store pairs of (temperature, index)
        stack = []  # Monotonic decreasing stack
        
        # Iterate over the temperature list with index
        for i, t in enumerate(temperatures):
            # While stack is not empty and current temperature is greater
            # than the temperature at the top of the stack
            while stack and t > stack[-1][0]:  
                stackt, stackInd = stack.pop()  # Pop the last stored temperature and index
                res[stackInd] = (i - stackInd)  # Calculate the days until a warmer temp
            
            # Push the current temperature and index onto the stack
            stack.append([t, i])  
        
        return res  