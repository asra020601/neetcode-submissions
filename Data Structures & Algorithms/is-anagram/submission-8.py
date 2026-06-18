class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two dicts for two strings
        count_s  = {}
        count_t  = {}
        for i in s: #this is n for time complexity but we will discuss that later lets find the solution first
            count_s[i]=count_s.get(i,0)+1 #counting the frequency of each element in s string 
        for i in t:
            count_t[i]=count_t.get(i,0)+1 #counting the frequency of each element in t string
        #now we compare the keys and values of count_s and count_t if these two are the same then we have return True since this is an anagram
        #else we return False, for now we are assuming that s and t are always the same length.
        all_chars = str(count_s.keys())+str(count_t.keys())

        for i in all_chars:#how do i check for each element in s and t?
            if i in count_s and i in count_t: #if the key exists in both we compare the values, if it doesn'tthen we say print(False)
                    if count_s[i]!=count_t[i]:
                       return(False)
            elif i in count_s or i in count_t:
                return(False)
        return(True)