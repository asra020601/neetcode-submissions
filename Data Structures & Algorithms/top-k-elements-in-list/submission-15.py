class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic1 ={}
        for i in range(len(nums)):
            dic1[nums[i]]=dic1.get(nums[i],0)+1
        heap  =[]
        for key,value in dic1.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
       