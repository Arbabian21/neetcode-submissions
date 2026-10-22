from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = defaultdict(list)
        for word in strs:
            letterOccurances = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                letterOccurances[index] += 1
            dictionary[tuple(letterOccurances)].append(word)

        return list(dictionary.values())
            

