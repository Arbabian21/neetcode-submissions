# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(len(pairs)):
            # i is equal to the new number we are adding to the sorted portion (sorted from index 0 to i-1)
            j = i -1 # upper bound of the sorted portion

            while j >= 0 and pairs[j+1].key < pairs[j].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            res.append(pairs[:])

        return res