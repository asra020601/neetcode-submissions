class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 ={}
        for i in range(0,len(nums)):
            if nums[i] in nums2.keys():
                return True
            else:
                nums2[nums[i]]=nums2.get(nums[i],0)+1
                if nums2[nums[i]]>1:
                    return True
        return False