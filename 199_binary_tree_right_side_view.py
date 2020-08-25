# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        rst = []
        queue = [(root, 0)]

        while queue:
            item = queue.pop(0)
            node = item[0]
            if node is None:
                continue
                
            depth = item[1]
            if len(rst) == depth:
                rst.append(node.val)
            queue.append((node.right, depth + 1))
            queue.append((node.left, depth + 1))

        return rst


if __name__ == '__main__':
    Solution().rightSideView(TreeNode(1))
