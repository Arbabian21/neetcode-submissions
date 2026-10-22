# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        sortedBST = self.inOrderTraversal(root)
        if len(sortedBST) < k < 0: return None
        for i in sortedBST: print(i.val)
        return sortedBST[k-1].val

    
    def inOrderTraversal(self, root, visited=None):
        if visited is None: visited = []
        if not root: return visited

        self.inOrderTraversal(root.left, visited)
        visited.append(root)
        self.inOrderTraversal(root.right, visited)
        return visited

