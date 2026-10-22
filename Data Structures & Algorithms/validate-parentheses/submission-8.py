class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingBracketDictionary = {"]":"[", "}":"{", ")":"("}

        for bracket in s:
            if bracket in closingBracketDictionary:
                if stack and stack[-1] == closingBracketDictionary[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
            
        return True if not stack else False