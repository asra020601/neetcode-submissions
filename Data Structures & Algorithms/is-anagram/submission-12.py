class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s): return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]=count[ord(s[i])-ord('a')]+1
            count[ord(t[i])-ord('a')]=count[ord(t[i])-ord('a')]-1
        for element in count:
            if element!=0:
                return False
        return True