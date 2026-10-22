class Solution:
    def rob(self, nums: List[int]) -> int:
        

        return max(nums[0], self.helpRob(nums[:len(nums)-1]), self.helpRob(nums[1:]))
    
    def helpRob(self, portionOfNums):
            rob1, rob2 = 0,0

            for value in portionOfNums:
                temp = max(value + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2