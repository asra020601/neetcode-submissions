class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = []
        for height in range(len(heights)):
            l = height
            r = height+1
            width = 0 
            while l>=0:
                if heights[l]>=heights[height]:
                    l =l-1
                    width = width+1#i need to make sure this doesn't change with every iteration
                else: break
            while r<len(heights):
                if heights[r]>=heights[height]:
                    width = width+1#i do not understand why we are getting 8 and 9 here when the len(heights) is only
                    r =r+1
                else: break
            res.append(width)
        res = [i * j for i, j in zip(res, heights)]
        return max(res)
        