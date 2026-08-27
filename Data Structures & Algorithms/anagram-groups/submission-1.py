class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = {}
        for item in strs:
            sorted_item = "".join(sorted(item))
            if sorted_item not in output_dict:
                output_dict[sorted_item] = [item]
            else: 
                output_dict[sorted_item].append(item)
        return [value for value in output_dict.values()]