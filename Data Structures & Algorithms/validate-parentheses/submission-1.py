class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if p == "]" and stack and stack[-1] == "[":
                    stack.pop()
                elif p == ")" and stack and stack[-1] == "(":
                    stack.pop()
                elif p == "}" and stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return not stack