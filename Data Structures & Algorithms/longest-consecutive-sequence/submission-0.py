class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        def recur(x,length):
            if x+1 in nums:
              return recur(x+1,length+1)
            return length
        for i in range(len(nums)):
           length = recur(nums[i],1)
           if length>max_length:
              max_length = length
        return max_length