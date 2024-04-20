class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in brackets:
                stack.append(c)
            elif len(stack)==0 or brackets[stack.pop()] != c:
                return False
        if len(stack)==0:
            return True
        else:
            return False
        