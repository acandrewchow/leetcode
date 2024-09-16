from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Uses bucket sort for O(n)
        # key value pairs that determine the count and frequency
        # stops at the value of k
        # i.e input: nums = [1, 1, 1, 2, 2, 3], k = 2
        # output: [1, 2]
        # count [ [0] [1] [2] [3] [4] [5] [6] ]
        # values[ [100] [3] [2] [1] [0] ]
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
     
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            # freq = [[], [3], [2], [1], [], [], []]
            freq[c].append(n) 

        res = []
   
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        