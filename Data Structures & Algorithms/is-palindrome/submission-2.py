class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        s = list((i.lower() for i in s if i in alphabet))
        l = 0
        r  = len(s)-1
        while l<r:
            if s[l]!=s[r]:
               return(False)
            else:
                l = l+1
                r = r-1
        return(True)