class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for number in nums:
            dictionary[number] = 1 + dictionary.get(number, 0)
        
        bucketSort = [[] for i in range(len(nums) + 1)]
        print(bucketSort)

        for number, frequency in dictionary.items():
            bucketSort[frequency].append(number)

        res = []

        for row in range(len(bucketSort)-1, -1, -1):
            for col in range(len(bucketSort[row])):
                res.append(bucketSort[row][col])
                if len(res) == k: return res

        
            
