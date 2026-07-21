class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r =1, max(piles)
        while l<=r:
            mid = (l+r)//2
            k = mid
            time_spent = 0
            for i in range(len(piles)):
                time_spent = time_spent+math.ceil(piles[i]/k)
            if time_spent > h:
                l = mid+1
            else:
                r = mid-1
        return l