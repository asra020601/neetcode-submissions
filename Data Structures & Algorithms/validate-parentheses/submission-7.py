class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '[':']','{':'}'}
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if not stack:
                    return False
                closing = stack.pop()
                if brackets[closing]!=i:
                    return False
        return len(stack)==0


