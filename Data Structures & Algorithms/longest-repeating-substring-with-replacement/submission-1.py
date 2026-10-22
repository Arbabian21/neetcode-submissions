class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countEachLetter = dict()
        longestSubstringLength = 0  

        left, maxFrequency = 0, 0
        for right in range(len(s)):
            countEachLetter[s[right]] = 1+ countEachLetter.get(s[right],0)
            maxFrequency = max(maxFrequency, countEachLetter[s[right]])

            while (right-left+1) - maxFrequency > k:
                countEachLetter[s[left]] = countEachLetter.get(s[left],0) -1 
                left += 1

            longestSubstringLength = max(longestSubstringLength, (right-left+1))
        
        return longestSubstringLength
