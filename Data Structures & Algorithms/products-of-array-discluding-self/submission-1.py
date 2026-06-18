class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 0
        ans = []
        while x <len(nums):
          postfix = 1
          prefix = 1
          for i in range(x,len(nums)-1):
              postfix = postfix * nums[i+1]
          for j in range(0,x):
              prefix = prefix * nums[j]
          product = postfix *prefix
          ans.append(product)
          x = x+1
        return ans