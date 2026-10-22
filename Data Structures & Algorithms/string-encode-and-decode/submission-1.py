class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            wordLength = int(s[i:j])
            res.append(s[j+1: j + 1 + wordLength])
            i = j+1+wordLength
        return res
            

