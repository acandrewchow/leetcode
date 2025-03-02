from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        modified_nums = []

        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
       
        for num in nums:
            if num != 0:
                modified_nums.append(num)

        while len(modified_nums) < len(nums):
            modified_nums.append(0)

        return modified_nums


        