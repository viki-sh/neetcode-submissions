class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_dict = {}
        for i,v in enumerate(nums):
            remainder = target - v
            if remainder in index_dict:
                return [index_dict[remainder],i]
            else: 
                index_dict[v] = i
            




        



