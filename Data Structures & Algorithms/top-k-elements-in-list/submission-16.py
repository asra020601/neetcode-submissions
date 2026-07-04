class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic1 ={}
        for i in range(len(nums)):
            dic1[nums[i]]=dic1.get(nums[i],0)+1
        freq =[[] for i in range(len(nums)+1)]
        for key,value in dic1.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            for element in freq[i]:
                res.append(element)
                if len(res)==k:
                    return res