class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        for element in nums:
            count[element] = count.get(element,0)+1
        for ele, freq in count.items():
            frequency[freq].append(ele)
        res = []
        for i in range(len(frequency)-1,0,-1):
            for element in frequency[i]:
                res.append(element)
                if len(res)==k:
                    return res