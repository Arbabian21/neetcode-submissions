class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if self.isItAlNum(s[left]) and self.isItAlNum(s[right]):
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
            elif not self.isItAlNum(s[left]):
                left += 1
            elif not self.isItAlNum(s[right]):
                right -= 1
        return True

    def isItAlNum(self, letter):
        ascii = ord(letter)
        if 48 <= ascii <= 57 or  65 <= ascii <= 90 or 97 <= ascii <= 122:
            return True
        return False