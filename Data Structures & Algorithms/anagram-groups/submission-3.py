class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp =  defaultdict(list)
        for i in range(len(strs)):
            freq = {}
            for j in range(len(strs[i])):
                freq[strs[i][j]] = freq.get(strs[i][j],0)+1
            freq = tuple(sorted(freq.items()))
         
            mapp[freq].append(strs[i])
        return list(mapp.values())