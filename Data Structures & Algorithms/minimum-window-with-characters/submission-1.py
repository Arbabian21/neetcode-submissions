class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        targetCount = dict()
        windowCount = dict()

        result = [-1,-1]
        resultLen = float("infinity")

        for character in t:
            targetCount[character] = 1 + targetCount.get(character, 0)
        

        have, need = 0, len(targetCount)
        left = 0
        for right in range(len(s)):
            currentChar = s[right]
            windowCount[currentChar] = 1 + windowCount.get(currentChar, 0)

            if currentChar in targetCount:
                if windowCount[currentChar] == targetCount[currentChar]:
                    have += 1

            while have == need:
                if resultLen > right-left+1:
                    resultLen = right-left+1
                    result = [left, right]

                windowCount[s[left]] -= 1
                if s[left] in targetCount:
                    if windowCount[s[left]] < targetCount[s[left]]:
                        have -= 1
                left += 1

        left, right = result
        return s[left: right+1] if resultLen != float("infinity") else ""
