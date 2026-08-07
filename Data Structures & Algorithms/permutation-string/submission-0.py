class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
           return False
        l,r =0,0
        freqs1 ={}
        freqs2= {}
        for i in range(len(s1)):
           freqs1[s1[i]]=freqs1.get(s1[i],0)+1
        while r<len(s2):
            freqs2[s2[r]]=freqs2.get(s2[r],0)+1
            if (r-l+1)>len(s1):
                freqs2[s2[l]]=freqs2[s2[l]]-1
                if freqs2[s2[l]]==0:
                   del freqs2[s2[l]]
                l = l+1
            if freqs1==freqs2:
               return True
            r = r+1
        return False
