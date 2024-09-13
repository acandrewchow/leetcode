from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)
             # Compare middle element with the next element
            if nums[m] > nums[m + 1]:  # If the mid element is greater than the next, peak lies on the left side
                r = m
            else:
                l = m + 1 # if not, peak lies on the right side
        return l
    
# examples:
# [1, 4, 3, 2, 1] - peak is 4
if __name__ == "__main__":
    nums = [1, 4, 3, 2, 1]
    sol = Solution()
    peak_index = sol.findPeakElement(nums)
    print(f"Peak element index: {peak_index}, Peak element value: {nums[peak_index]}")