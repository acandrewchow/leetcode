from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target: # on the left side
                r = m - 1
            elif nums[m] < target: # on the right side 
                l = m + 1
            else:
                return m
        return -1
    
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Target is present in the array
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    result1 = sol.search(nums1, target1)
    print(f"Example 1: Target {target1} found at index {result1}")  # Output: 4

    # Example 2: Target is not present in the array
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    result2 = sol.search(nums2, target2)
    print(f"Example 2: Target {target2} found at index {result2}")  # Output: -1

    # Example 3: Target is the first element
    nums3 = [1, 2, 3, 4, 5]
    target3 = 1
    result3 = sol.search(nums3, target3)
    print(f"Example 3: Target {target3} found at index {result3}")  # Output: 0

    # Example 4: Target is the last element
    nums4 = [1, 2, 3, 4, 5]
    target4 = 5
    result4 = sol.search(nums4, target4)
    print(f"Example 4: Target {target4} found at index {result4}")  # Output: 4

    # Example 5: Single element array, target is present
    nums5 = [10]
    target5 = 10
    result5 = sol.search(nums5, target5)
    print(f"Example 5: Target {target5} found at index {result5}")  # Output: 0

    # Example 6: Single element array, target is not present
    nums6 = [10]
    target6 = 5
    result6 = sol.search(nums6, target6)
    print(f"Example 6: Target {target6} found at index {result6}")  # Output: -1