class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res  = defaultdict(list) #here the values will be the strings in the strs list, and the keys will the count of 26 letters in each those strongs
        for s in strs : #looping through the list
            count = [0]*26#each loop gets the 'key' of 26 letters
            for c in s:#looping through each string
                count[ord(c)-ord('a')]+=1#calculating which position to increment and incrementing it
            res[tuple(count)].append(s) #if we already have the count we add the "values" to the same "key" and if we have a new count we create a new "key"-> the string in the list (act, tap)
        return list(res.values())#returning the values after the loop ends
