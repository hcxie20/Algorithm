'''
recursive:
max_gain: maximun length of a path covering this node
'''
class Solution:
    def maxPathSum(self, root) -> int:
        rst = -float('inf')

        def max_gain(node):
            nonlocal rst
            node_path = node.val

            if node.left is None and node.right is None:
                rst = max(rst, node.val)
                return node.val

            elif node.right is None:
                left = max_gain(node.left)
                if left > 0:
                    node_path += left
                rst = max(rst, node_path)
                return node_path

            elif node.left is None:
                right = max_gain(node.right)
                if right > 0:
                    node_path += right
                rst = max(rst, node_path)
                return node_path
            
            else:
                left = max_gain(node.left)
                right = max_gain(node.right)
                for num in [left, right]:
                    if num > 0:
                        node_path += num
                rst = max(rst, node_path)
                
                if node_path > node.val:
                    return node.val + max(left, right)
                else:
                    return node.val
        max_gain(root)
        return rst
