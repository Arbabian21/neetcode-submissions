class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCapacity, left, right = 0, 0, len(heights)-1
        while left < right:
            limitingCapacity = min(heights[left], heights[right])
            currentMaxCapacity = limitingCapacity * (right-left)
            maxCapacity = max(currentMaxCapacity,maxCapacity)

            if limitingCapacity == heights[left]:
                left += 1
            else:
                right -= 1
        
        return maxCapacity