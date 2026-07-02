class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1 ={}
        for index,element in enumerate(nums):
            complement  = target - element
            if complement in dic1:
                return [dic1[complement],index]
            dic1[element]=index
