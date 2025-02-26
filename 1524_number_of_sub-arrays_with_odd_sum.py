# O (n^2)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        currentSum = 0
        oddSums = []
        oddSubArrays = 0

        # [1, 3, 5]
        # [1], [1, 3], [1,3,5]
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarray = arr[i:j+1]
                totalSum = sum(subarray)
        
                if totalSum % 2 == 1:
                    print(totalSum)
                    oddSubArrays += 1
        return oddSubArrays

# O(n)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix_sum = 0
        odd_count = 0
        even_count = 1
        total_odd_subarrays = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                total_odd_subarrays += odd_count
                even_count += 1
            else:
                total_odd_subarrays += even_count
                odd_count += 1
            total_odd_subarrays %= MOD

        return total_odd_subarrays 







        





        