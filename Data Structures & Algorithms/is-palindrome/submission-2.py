class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for letter in s:
            if letter.isalnum():
                word += letter.lower()

        return word == word[::-1]