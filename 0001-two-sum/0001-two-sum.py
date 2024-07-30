class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}


        for index,value in enumerate(nums):
            if target-value not in dic:
                dic[value]=index
            else:
                return (dic[target-value],index)