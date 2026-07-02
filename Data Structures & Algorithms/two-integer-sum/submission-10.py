class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1 ={}
        for index,element in enumerate(nums):
            complement  = target - element
            if complement in dic1.keys():
                return sorted([index,dic1[complement]])
            dic1[element]=index
