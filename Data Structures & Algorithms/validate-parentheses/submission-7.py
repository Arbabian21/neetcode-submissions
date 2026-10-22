class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDictionary = {")" : "(", "]":"[","}":"{"}
        for bracket in s:
            if bracket in bracketDictionary:
                if stack and stack[-1] == bracketDictionary[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False