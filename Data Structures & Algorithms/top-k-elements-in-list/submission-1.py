class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberOccuranceDictionary = {}
        bucketSortByOccurance = [[] for i in range(len(nums) +1)]
        returnArr = []

        for i in nums:
            numberOccuranceDictionary[i] = 1 + numberOccuranceDictionary.get(i, 0)

        for (number, frequency) in numberOccuranceDictionary.items():
            bucketSortByOccurance[frequency].append(number)

        for i in range(len(bucketSortByOccurance)-1, 0, -1):
            for j in range(len(bucketSortByOccurance[i])):
                returnArr.append(bucketSortByOccurance[i][j])
                if len(returnArr) == k:
                    return returnArr