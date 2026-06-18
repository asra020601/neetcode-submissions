class Solution:

    def encode(self, strs: List[str]) -> str:
     res =""
     for i in strs:
        res = res+str(len(i))+"#"+i
     return res
    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j]!= "#":
                j = j+1
            l = int(s[i:j])
            output.append(s[j+1:j+1+l])
            i = j+1+l
        return output