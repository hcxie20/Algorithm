# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        node1 = None
        node2 = None
        last = None

        def inorder(node):
            nonlocal last, node1, node2
            if node.left:
                inorder(node.left)
            
            if last is not None and last.val > node.val:
                if node1 is None:
                    node1 = last
                
                node2 = node
            
            last = node


            if node.right:
                inorder(node.right)
        
        inorder(root)
        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val