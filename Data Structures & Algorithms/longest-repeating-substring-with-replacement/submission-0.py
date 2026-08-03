class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        seen={}
        maxx =0
        maxf =0 
        while r<len(s):
            seen[s[r]]=seen.get(s[r],0)+1
            maxf = max(maxf, seen[s[r]])
            while (((r-l)+1) - maxf) > k:
                #shrink the window and subtract the frequency bu one
                seen[s[l]]=seen.get(s[l],0)-1
                l = l+1
            maxx = max((r-l)+1,maxx)
            r = r+1
        return maxx