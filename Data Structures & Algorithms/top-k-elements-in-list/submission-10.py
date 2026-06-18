class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        sorted_items = sorted(freq.items(), key = lambda x:x[1])
        res =  [items[0] for items in sorted_items[-k:]]
        return res