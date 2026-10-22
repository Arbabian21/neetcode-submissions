class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        outputList = []
        for index, element in enumerate(nums):
            if (target - element) not in dictionary.keys():
                dictionary[element] = index
            else :
                outputList.append(dictionary[target-element])
                outputList.append(index)

        
        # for key, value in dictionary.items():
        #     otherParam = target-key
        #     if otherParam in dictionary.keys():
        #         if dictionary[other]
        #         outputList.append(value)
        #         outputList.append(dictionary[otherParam])
        
        return outputList
                
