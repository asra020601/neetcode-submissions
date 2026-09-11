class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create minifreq for each word if that freq exists as a key in the freq hashmap we add the word to as value, if it doesnt we create the key and add the value (word) in the end we append all the words as lists in one list
        freq ={}
        for i in range(len(strs)):
            minifreq ={}
            for char in strs[i]:
                minifreq[char]=minifreq.get(char,0)+1
            #convert minifreq to tuple so we can save it as key
            keyfreq = tuple(sorted(minifreq.items()))
            if keyfreq in freq:
                freq[keyfreq].append(strs[i])
            else:
                freq[keyfreq]=[strs[i]]
        return list(freq.values())