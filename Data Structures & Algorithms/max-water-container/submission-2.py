class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            j = i+1
            while j<len(heights):
              h = min(heights[i],heights[j])
              w = (j+1)-(i+1)
              area =  max(area,h*w)
              j = j+1
        return area