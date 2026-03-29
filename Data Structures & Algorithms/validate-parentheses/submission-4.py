class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for brack in s:
            if brack in ('{','[','('):
                stack.append(brack)
            else:
                if not stack:
                    return False
                elif brack == '}' and stack.pop() != '{':
                    return False
                elif brack == ']' and stack.pop() != '[':
                    return False
                elif brack == ')' and stack.pop() != '(':
                    return False
        
        if stack:
            return False
        
        return True
        