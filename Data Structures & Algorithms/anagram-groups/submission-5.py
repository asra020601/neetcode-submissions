class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic1  = {}
        for i in range(len(strs)):
           freq = [0]*26
           for char in strs[i]:
            freq[ord(char)-ord('a')]=freq[ord(char)-ord('a')]+1
           key = tuple(freq)
           if key in dic1:
            dic1[key].append(strs[i])
           else:
            dic1[key]=[strs[i]]
        return list(dic1.values())