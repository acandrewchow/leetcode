from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_list = []
        equal_list = []
        larger_list = []

        # iterates through nums and maintains order
        for num in nums:  
            if num < pivot:
                smaller_list.append(num)
            elif num == pivot:
                equal_list.append(num)
            else:
                larger_list.append(num)

        return smaller_list + equal_list + larger_list