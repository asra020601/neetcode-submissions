class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r =0,0
        seen = set()
        maximum = 0
        while r<len(s):
            while s[r] in seen:
                
                seen.remove(s[l])
                l = l+1
            maximum = max((r-l)+1,maximum)
            seen.add(s[r])
            r = r+1
        return maximum