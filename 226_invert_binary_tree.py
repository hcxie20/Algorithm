# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def invertChild(node):
            if not node:
                return 
            
            node.left, node.right = node.right, node.left
            invertChild(node.left)
            invertChild(node.right)

        invertChild(root)
        return root