class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output =  output+i+";"
        return output
    def decode(self, s: str) -> List[str]:
        decoded = []
        second  = ""
        for j in range(len(s)):
            if s[j]==";":
                decoded.append(second)
                second=""
            else:
                second = second + s[j]
        return decoded
