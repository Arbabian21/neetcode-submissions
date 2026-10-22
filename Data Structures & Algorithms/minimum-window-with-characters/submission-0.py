class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countTarget, windowDictionary = {},{}
        result, resultLength = [-1,-1], float("infinity")
        left = 0

        for char in t:
            countTarget[char] = countTarget.get(char, 0) + 1
        
        have, need = 0, len(countTarget)

        for right in range(len(s)):
            currentChar = s[right]
            windowDictionary[currentChar] = 1 + windowDictionary.get(currentChar, 0)

            if currentChar in countTarget and windowDictionary[currentChar] == countTarget[currentChar]:
                have += 1
            
            while have == need:
                if (right-left+1) < resultLength:
                    resultLength = right-left+1
                    result = [left, right]

                windowDictionary[s[left]] -= 1
                if s[left] in countTarget and windowDictionary[s[left]] < countTarget[s[left]]:
                    have -= 1
                
                left += 1
            
        left, right = result
        return s[left:right+1] if resultLength != float("infinity") else ""
            

