class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans  = []
        for i in range(len(nums)):
            b = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==b:               
                   ans.append(i)
                   ans.append(j)
        return ans