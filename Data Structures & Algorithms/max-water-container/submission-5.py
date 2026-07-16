class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        i = 0
        j = len(heights)-1
        while i<len(heights)-1:
            curr= min(heights[i],heights[j]) * (j-i)
            largest  = max(curr,largest)
            if heights[i]<max(heights):
                i = i+1
            elif heights[j]<max(heights):
                j = j-1
            else:
                curr= min(heights[i],heights[j]) * (j-i)
                largest  = max(curr,largest)
                return largest
            curr= min(heights[i],heights[j]) * (j-i)
            largest  = max(curr,largest)

        return largest