# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        rst = []


        def preorder(node, level):
            if len(rst) < level + 1:
                rst.append([])
            
            if level % 2 == 0:
                rst[level].append(node.val)
            else:
                rst[level].insert(0, node.val)

            if node.left:
                preorder(node.left, level+1)
            if node.right:
                preorder(node.right, level+1)

        
        preorder(root, 0)
        return rst