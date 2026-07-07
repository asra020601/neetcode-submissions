class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        #but how do i calculate the product 
        for i in range(len(nums)):
            pre = 1
            post = 1
            j = i+1
            while j<len(nums):
                post = post*(nums[j])
                j = j+1
            k = i-1
            while k>-1:
                pre = pre*(nums[k])
                k = k-1
            res.append(pre*post)
        return res