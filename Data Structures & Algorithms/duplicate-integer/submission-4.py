class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)# O of N(logN)) time complexity
        for i in range(len(nums)-1):#O of N-1 time complexity
            if nums[i]==nums[i+1]:#O of N time complexity
                return True
        return False