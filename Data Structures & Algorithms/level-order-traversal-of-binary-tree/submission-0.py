# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            currLevel = []
            queueLen = len(queue)

            for _ in range(queueLen):
                curr = queue.popleft()
                if curr:
                    currLevel.append(curr.val)
                    if curr.left: queue.append(curr.left)
                    if curr.right: queue.append(curr.right)
            if currLevel:
                result.append(currLevel)
        return result