# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return "N"
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if type(curr) == TreeNode: 
                res.append(str(curr.val))
            else:
                res.append(curr)

            if type(curr) == TreeNode:
                if curr.left: 
                    queue.append(curr.left)
                else:
                    queue.append("N")
                if curr.right: 
                    queue.append(curr.right)
                else:
                    queue.append("N")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        if data[0] == "N": return None

        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1
        while queue:
            curr = queue.popleft()
            if data[index] != "N":
                curr.left = TreeNode(int(data[index]))
                queue.append(curr.left)
            index += 1
            if data[index] != "N":
                curr.right = TreeNode(int(data[index]))
                queue.append(curr.right)
            index += 1
        return root

        