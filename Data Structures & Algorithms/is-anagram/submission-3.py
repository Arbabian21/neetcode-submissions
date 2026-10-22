class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sDictionary = {}
        for letter in s:
            sDictionary[letter] = 1 + sDictionary.get(letter, 0)

        tDictionary = {}
        for letter in t:
            tDictionary[letter] = 1 + tDictionary.get(letter, 0)

        return sDictionary == tDictionary
