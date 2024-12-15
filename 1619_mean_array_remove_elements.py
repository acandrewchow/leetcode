class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sorted_list = sorted(arr)
        
        elements = len(arr)
        num_to_remove = int(elements * 0.05)

        trimmed_list = sorted_list[num_to_remove: -num_to_remove]
        
        mean = sum(trimmed_list) / len(trimmed_list)

        return mean