class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = {}

        for i in nums:
            occurances[i] = occurances.get(i,0) + 1
        
        tuplesOfOccurances = ((frequency, number) for (number, frequency) in occurances.items())
        tuplesOfOccurances = sorted(tuplesOfOccurances)

        kMostElements = []
        for i in range(k):
            kMostElements.append(tuplesOfOccurances.pop()[1])

        return kMostElements