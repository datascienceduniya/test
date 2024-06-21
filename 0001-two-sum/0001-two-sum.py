class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}


        for index,values in enumerate(nums):
            if target - values not in dic:
                dic[values]=index

            else:
                return [dic[target-values],index]