class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1] 
        for i in range(len(nums)):
            pre.append(pre[i]*nums[i])
        j = 0
        for i in range(len(nums)-1,-1,-1):
          post.append(post[j]*nums[i])
          j = j+1
        post = post[::-1]
        product = []
        i = 0
        while i<len(post)-1:
           product.append(pre[i]*post[i+1])
           i = i+1
        return product