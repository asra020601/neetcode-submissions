class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        i = 0
        j = len(heights)-1
        while i<=j:
            curr= min(heights[i],heights[j]) * (j-i)
            largest  = max(curr,largest)

            if heights[i]<heights[j]:
                i = i+1
            else:
                j=j-1

        return largest