class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterCountDict = {}
        longest = 0
        maxFrequency = 0
        left = 0

        for right in range(len(s)):
            letterCountDict[s[right]] = 1 + letterCountDict.get(s[right], 0)
            maxFrequency = max(maxFrequency, letterCountDict[s[right]])

            while (right-left+1) - maxFrequency > k:
                letterCountDict[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)
        
        return longest