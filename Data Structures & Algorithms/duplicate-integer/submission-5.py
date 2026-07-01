class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        #traverse through each element in the nums list and append it to seen set
        #before appending we ask if this element already exists in the set 
        #if it does we output True else we move on
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False