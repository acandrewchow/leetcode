from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            diff = numbers[l] + numbers[r]

            if diff > target:
                r -= 1
            elif diff < target: 
                l += 1
            else:
                return [l + 1, r + 1]
        

solution = Solution()
numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9

print(solution.twoSum(numbers, target))
