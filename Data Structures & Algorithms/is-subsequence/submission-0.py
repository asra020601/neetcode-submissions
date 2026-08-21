class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0 #only move this when s[pointer_s] has been found in t, if s ends, it means everything has been found. if t ends and s doesnt return False
        i = 0
        while i<len(t):
            if pointer_s>=len(s):
                return True
            if s[pointer_s]==t[i]:
                pointer_s=pointer_s+1
            i = i+1
        return pointer_s == len(s)