class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans  = [0] * len(arr)
        curr_max  = -1
        #we calculate curr_max with every arr[i]
        for i in range(len(arr)-1,-1,-1):
            ans[i]=curr_max
            curr_max=max(curr_max,arr[i])
        return ans