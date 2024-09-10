from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # Profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # Found a lower price to buy
                l = r
            r += 1
        return maxP

if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Increasing Prices
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = sol.maxProfit(prices1)
    print(f"Test case 1: Max profit = {result1}")  # Expected Output: 5

    # Test case 2: No profit (prices decreasing)
    prices2 = [7, 6, 4, 3, 1]
    result2 = sol.maxProfit(prices2)
    print(f"Test case 2: Max profit = {result2}")  # Expected Output: 0

    # Test case 3: Mixed prices with multiple peaks
    prices3 = [3, 2, 6, 5, 0, 3]
    result3 = sol.maxProfit(prices3)
    print(f"Test case 3: Max profit = {result3}")  # Expected Output: 4