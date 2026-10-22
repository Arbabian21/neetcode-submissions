class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        maxLen = 0

        for i in range(len(s)):

            # odd length
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    result = s[left:right+1]
                    maxLen = right-left+1
                left -= 1
                right += 1

            # even length
            left, right = i, i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    result = s[left:right+1]
                    maxLen = right-left+1
                left -= 1
                right += 1

        return result