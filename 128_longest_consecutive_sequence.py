from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        print(num_set)

        for num in num_set:
            if (num - 1) not in num_set: # no neighbor, therefore start of sequence
                length = 1
                while (num + length) in num_set: 
                    length += 1
                longest = max(length, longest)
        return longest
        

solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(solution.longestConsecutive(nums))    