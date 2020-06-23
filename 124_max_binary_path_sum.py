'''
recursive:
max_gain: maximun length of a path covering this node
'''
class Solution:
    def maxPathSum(self, root) -> int:
        rst = -float('inf')

        def max_gain(node):
            nonlocal rst
            if node.left is None and node.right is None:
                rst = max(rst, node.val)
                return node.val

            node_gain = node.val

            if node.left:
                left = max_gain(node.left)
                if left > 0:
                    node_gain += left

            if node.right:
                right = max_gain(node.right)
                if right > 0:
                    node_gain += right
            
            rst = max(rst, node_gain)
            
            return node_gain

        max_gain(root)
        return rst
