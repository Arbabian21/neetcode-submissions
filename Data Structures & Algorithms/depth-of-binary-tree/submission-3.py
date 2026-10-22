# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # iterative BFS
        # if not root: return 0
        # level = 0
        # queue = deque([root])
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1
        # return level
        if not root: return 0
        stack = [[root, 1]]
        maxDepth = 0
        while stack:
            for i in range(len(stack)):
                node, currLevel = stack.pop()
                maxDepth = max(maxDepth, currLevel)
                if node.left:
                    stack.append([node.left,currLevel+1])
                if node.right:
                    stack.append([node.right,currLevel+1])
        return maxDepth
             