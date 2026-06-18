class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1: return False
        stack = []
        closed = "}])"
        mapone = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
           if i in mapone: #if we encounter a closing bracket
            if stack and stack[-1]==mapone[i]:#if the opening bracket in the stack.pop() has a value that is equal to i
       #then we pop the bracket:
                stack.pop()
            else:
                return False
           else:
              stack.append(i) 
        return (True) if not stack else False