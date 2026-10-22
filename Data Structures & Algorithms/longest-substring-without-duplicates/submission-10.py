class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstringLength, start = 0, 0
        seenLetters = set()

        for end in range(len(s)):
            while s[end] in seenLetters:
                seenLetters.remove(s[start])
                start += 1
            seenLetters.add(s[end])
            longestSubstringLength = max(longestSubstringLength, (end-start+1))
        return longestSubstringLength
