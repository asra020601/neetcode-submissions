class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans  = []
        curr_max  = 0
        #we calculate curr_max with every arr[i]
        #if arr[i] > curr_max curr_max = arr[i]
        for i in range(len(arr)-1):
            curr_max = max(arr[i+1:])
            ans.append(curr_max)
        ans.append(-1)
        return ans