# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True
        # inorder
        self.last = None
        return self.inorder(root)

    def inorder(self, root):
        if root.left:
            if not self.inorder(root.left):
                return False

        if not self.last is None and root.val <= self.last:
            return False
        else:
            self.last = root.val

        if root.right:
            if not self.inorder(root.right):
                return False

        return True