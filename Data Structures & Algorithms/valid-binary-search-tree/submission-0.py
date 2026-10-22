# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #bfs but with array as entries
        if not root: return True
        queue = deque()
                    # currentNode, minimumValue, maximumValue
        queue.append([root, float("-inf"), float("inf")])
        while queue:
            curr, minimum, maximum = queue.popleft()
            if not (minimum < curr.val < maximum):
                return False
            if curr.left: queue.append([curr.left, minimum, curr.val])
            if curr.right: queue.append([curr.right, curr.val, maximum])

        return True