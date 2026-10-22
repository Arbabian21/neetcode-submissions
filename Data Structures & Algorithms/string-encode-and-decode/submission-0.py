class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedWord = ""
        for word in strs:
            encodedWord += str(len(word)) + "#" + word
        
        return encodedWord

    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            decodedList.append(word)
            i = j+1+length
        return decodedList