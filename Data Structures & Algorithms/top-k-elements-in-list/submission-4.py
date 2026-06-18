class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]# for counting the frequency and later adding to the keys to the count
        count = {}#we will populate this 
        for n in nums:#looping through each element
            count[n] = count.get(n,0)+1#getting the count of each object
        for c, n in count.items():
            freq[n].append(c)# populating the frequency array according to the count
        res  = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
