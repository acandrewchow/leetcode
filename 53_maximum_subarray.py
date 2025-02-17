from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0 

        for n in nums: 
            # check for negative prefix and reset sum to 0
            if curSum < 0:
                curSum = 0
            # increment our current sub, and update our max each time
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
