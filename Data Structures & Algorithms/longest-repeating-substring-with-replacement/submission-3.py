class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = dict()
        longestSubstring = 0
        
        left = 0
        for right in range(len(s)):
            seen[s[right]] = 1 + seen.get(s[right], 0)
            while (right-left+1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1

            longestSubstring = max(longestSubstring, (right-left+1))

        return longestSubstring