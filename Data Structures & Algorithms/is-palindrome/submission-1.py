class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha ="abcdefghijklmnopqrstuvwxyz"
        s = ''.join(
        ch for ch in s.lower() if ch in alpha or ch.isdigit())
        l = 0
        r = len(s)-1
        while l<r:
          if s[l]!=s[r]:
             return(False)
          l+=1
          r-=1
        return True
        