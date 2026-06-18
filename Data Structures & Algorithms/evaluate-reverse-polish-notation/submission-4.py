class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        for i in range(0,len(tokens)):
            if  tokens[i] in "+*/-":
                if tokens[i]=="+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif tokens[i]=="*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                elif tokens[i]=="-":
                   a = stack.pop()
                   b = stack.pop()
                   stack.append(b-a)
                else:
                   a = stack.pop()
                   b = stack.pop()
                   stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))   
        return stack[-1] 