class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            freq=0
            for character in word:
                freq = freq+1
            s = s+str(freq)+'#'+str(word)

        return s
    def decode(self, s: str) -> List[str]:
            res = []
            #num ='0123456789'
            i= 0
            while i <len(s):
                j = i
                while s[j]!='#':
                    j = j+1
                
                c = int(s[i:j])
                ele = ""
                start = j+1
                ele = ele+s[start:start+c]
                res.append(ele)
                i = start+c
            return res