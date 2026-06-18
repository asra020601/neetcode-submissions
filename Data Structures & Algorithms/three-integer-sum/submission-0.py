class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):#the 'k' loop for all elements 
            if i>0 and nums[i]==nums[i-1]:#no duplicates and i=0 executes so l starts at 1
                continue
            l = i+1#always one step aheaad of i 
            r = len(nums)-1 #last element
            while l<r:
                s = nums[l]+nums[r]+nums[i]
                if s==0:
                    res.append([nums[l], nums[r], nums[i]])#appending output
                    l = l+1 #changing the position since we got our result
                    r = r-1
                    while l<r and nums[r]==nums[r+1]: #avoiding duplicates 
                      r = r-1 #updating the right position
                    while l<r and nums[l]==nums[l-1]: #avoiding duplicates
                      l = l+1 #update till we find a distinct position
                elif s>0:
                    r = r-1
                else:
                    l = l+1
        return res

                


