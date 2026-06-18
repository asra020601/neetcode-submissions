class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre  = [0]*(len(nums))
        product = []
        pre[0]=1
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        post = [0]*len(nums)
        post [-1] = 1
        for i in range(len(nums)-1,0,-1):
           post[i-1]= post[i]*nums[i]
        for i in range(len(nums)):
           product.append(pre[i]*post[i])
        return product