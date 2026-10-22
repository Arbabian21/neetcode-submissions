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

        return self.merge(left, right)


    def merge(self, left, right):
        res = []
        l, r = 0, 0

        while l < len(left) or r < len(right):
            if l == len(left):
                res.extend(right[r:])
                break

            elif r == len(right):
                res.extend(left[l:])
                break

            elif left[l].key <= right[r].key:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

        return res




