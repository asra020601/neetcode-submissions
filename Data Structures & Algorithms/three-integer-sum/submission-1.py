class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums =sorted(nums)
        ans  = set()
        for i in range(len(nums)-1):
            j = i+1
            while j<len(nums):
                k = nums[i]+nums[j]
                if (k *-1) in nums:
                    index_k =  nums.index(-1*k)
                    if index_k != i and index_k!=j:
                        ans.add(tuple(sorted((nums[i], nums[j], -k))))

                j = j+1
        return list(ans)