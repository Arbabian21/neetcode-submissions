class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(heights)-1

        while left < right:
            currMinHeight = min(heights[left], heights[right])
            currWaterCapacity = currMinHeight * (right-left)
            maxWater = max(maxWater, currWaterCapacity)

            if currMinHeight == heights[left]: left += 1
            elif currMinHeight == heights[right]: right -= 1

        return maxWater