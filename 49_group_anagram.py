from typing import List
from collections import defaultdict

# Create a dictionary with values as a list
# Iterate through each string
    # Iterate for each character
    # Count the frequency for each character
    # Add the string to the tuple that corresponds to the same character frequency

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_map = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a.. z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            letter_map[tuple(count)].append(s)

        return letter_map.values()
        
# letter_map = {
#     (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'],
#     (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0): ['tan', 'nat'],
#     (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0): ['bat']
# }
