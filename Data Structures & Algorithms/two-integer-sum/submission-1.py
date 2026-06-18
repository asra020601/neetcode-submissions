class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap 
        hashmap = {}#creating a hashmap for output and memory
        for i, n in enumerate(nums):#i,n for index,value
            diff = target -n #n here is the value of each element in the given array
            if diff in hashmap: #if the difference already exists, we return the results
                return [hashmap[diff],i] # here we return the 'index' of the given 'diff' and the index of n from the array nums
            hashmap[n] = i # if it doesn't exist, the loop continues and adds the element to its respective index