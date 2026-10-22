class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for bracket in s:
            if bracket in closeToOpen.keys():
                if stack and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            elif bracket in closeToOpen.values():
                stack.append(bracket)
            else:
                return False

        return True if not stack else False
