class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a frequency hashmap
        freq ={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        #how do i sort this frequency dictionary you cant just sort a dictionary its not a lit
        #we convert this dictionary into a list a 2 dimension list
        arr = [] #list to store key,values in 2 dimensions
        for key,value in freq.items():
            arr.append([value,key])#we put value first because we need to sort it using values
        arr.sort() #sorted for value first
        arr = arr[-k:]
        result  = [v for i,v in arr] 
        return result   