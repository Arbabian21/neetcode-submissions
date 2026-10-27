class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        seen = dict()
        left = 0
        for right in range(len(s)):
            while seen.get(s[right], 0):
                seen[s[left]] -= 1
                left += 1

            seen[s[right]] = seen.get(s[right],0) +1
            longestSubstring = max(longestSubstring, right-left+1)

        return longestSubstring