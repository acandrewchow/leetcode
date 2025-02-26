class Solution:
    # Variation of Kadane's Algorithm
    # •	current_max keeps track of the maximum subarray sum ending at the current index
	# •	current_min keeps track of the minimum subarray sum ending at the current index
	# •	max_sum records the highest value of current_max encountered
	# •	min_sum records the lowest value of current_min encountered
	# •	By comparing max_sum and the absolute value of min_sum, we obtain the maximum absolute subarray sum
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_max = 0
        current_min = 0

        for n in nums:
            current_max = max(n, current_max + n)
            current_min = min(n, current_min + n)

            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

        return max(max_sum, abs(min_sum))
