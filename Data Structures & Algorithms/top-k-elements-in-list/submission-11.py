class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic1 ={}
        for i in range(len(nums)):
            dic1[nums[i]]=dic1.get(nums[i],0)+1
        res = sorted(dic1.keys(), key = lambda x:dic1[x])
        return res[-k:]
       