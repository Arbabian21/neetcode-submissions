class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False

        sdict, tdict = {}, {}
        for letter in s:
            sdict[letter] = sdict.get(letter, 0) + 1

        for letter in t:
            tdict[letter] = tdict.get(letter, 0) + 1

        return sdict == tdict