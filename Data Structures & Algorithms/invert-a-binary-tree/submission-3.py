# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        # solution 1
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root 

        # solution 2
        # tempNode = root.right
        # if root.left:
        #     root.right = self.invertTree(root.left)
        # else:
        #     root.right = None

        # if tempNode:
        #     root.left = self.invertTree(tempNode)
        # else:
        #     root.left = None
            
        # return root

        # solution 3
        tempNode = root.left
        root.left = root.right
        root.right = tempNode

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root