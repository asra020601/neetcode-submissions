class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxarea = 0
        while l<r:
            product = min(heights[l],heights[r])*(r-l)
            maxarea = max(product, maxarea)
            
            if heights[l]<heights[r]:
               l = l+1
            else:
                r = r-1
        return maxarea