# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        preorderIdx = 0
        
        def rebuild(inorderIdxL, inorderIdxR):
            nonlocal preorderIdx

            if inorderIdxL == inorderIdxR:
                return None
            
            root = TreeNode(preorder[preorderIdx])
            index = inorder.index(root.val)
            preorderIdx += 1
            root.left = rebuild(inorderIdxL, index)
            root.right = rebuild(index + 1, inorderIdxR)
            return root

        return rebuild(0, len(inorder))