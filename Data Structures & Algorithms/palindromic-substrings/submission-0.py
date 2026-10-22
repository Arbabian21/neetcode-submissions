class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):

            # odd length
            left, right = i, i
            oddCounter = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                oddCounter += 1
                left -= 1
                right += 1

            # even length
            left, right = i, i+1
            evenCounter = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                evenCounter += 1
                left -= 1
                right += 1

            counter += evenCounter + oddCounter
        return counter