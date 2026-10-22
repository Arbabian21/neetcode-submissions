# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1: return pairs

        middle = len(pairs)//2

        left = self.mergeSort(pairs[:middle])
        right = self.mergeSort(pairs[middle:])

        return self.merge(left,right)

    def merge(self, leftArr: List[Pair], rightArr: List[Pair]) -> List[Pair]:
        mergedArr: List[Pair] = []

        i, j = 0, 0

        while i < len(leftArr) or j < len(rightArr):
            if i == len(leftArr):
                mergedArr.extend(rightArr[j:])
                break
            if j == len(rightArr):
                mergedArr.extend(leftArr[i:])
                break
            
            if leftArr[i].key <= rightArr[j].key:
                mergedArr.append(leftArr[i])
                i += 1
            else:
                mergedArr.append(rightArr[j])
                j += 1
            
        return mergedArr
