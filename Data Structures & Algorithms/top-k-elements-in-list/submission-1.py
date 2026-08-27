class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_dict = {}
        for val in nums:
            if val not in counts_dict:
                counts_dict[val] = 1
            else: 
                counts_dict[val] +=1 
        
        sorted_dict = dict(sorted(counts_dict.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]
