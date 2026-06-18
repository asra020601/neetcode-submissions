class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs: #for each string in strs
            freq =[] #a list because we need to append
            for ch in i: #for each character in each string
                #we are creating the key for results (this is immutable)
                freq.append(ch)
            freq = tuple(sorted(freq))
        
            #if it exists in result keys we add the i to its values
            if freq in result:
                result[freq].append(i)#how do i add a list? + how to update a dictionary when the key already exists
            else:
                result[freq]=[i]
        return list(result.values())