class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionaryS, dictionaryT = {}, {}

        for i in range(len(s)):
            dictionaryS[s[i]] = 1 + dictionaryS.get(s[i], 0)
            dictionaryT[t[i]] = 1 + dictionaryT.get(t[i], 0)
        
        return dictionaryS == dictionaryT

        
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s = sorted(s)
#         t = sorted(t)
#         if s == t:
#             return True
#         return False
