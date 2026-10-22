from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for word in strs:
            alphabet = [0]*26
            for letter in word:
                asci = ord(letter.lower()) - ord("a")
                alphabet[asci] += 1
            alphabet = tuple(alphabet)
            dictionary[alphabet].append(word)
        
        return list(dictionary.values())

