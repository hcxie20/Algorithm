'''
Successor: WILL find the next key even there is multiple nodes with key value ONLY if node.left <= node and node.right >node
'''

import numpy as np

class TreeNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.p = None

class BinarySearchTree:
    def __init__(self, ls):
        self.root = None
        for i in range(len(ls)):
            self.insert(ls[i])

    def insert(self, key):
        z = TreeNode(key)
        y = None
        x = self.root
        while x != None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, key):
        x = self.root
        while x != None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def successor(self, node):
        if node.right != None:
            return self.min(node.right)
        y = node.p
        while y != None and node == y.right:
            node = y
            y = y.p
        return y

    def predecessor(self, node):
        if node.left != None:
            return self.max(node.left)
        y = node.p
        while y != None and node == y.left:
            node = y
            y = y.p
        return y

    def transplant(self, target, src):
        '''
        use node src in place of target
        Do not change the parent of src
        '''
        if target.p == None:
            # target = root
            self.root = src
        elif target == target.p.left:
            target.p.left = src
        else:
            target.p.right = src
        if src != None:
            src.p = target.p
    
    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            sccsr = self.min(node.right)
            if sccsr.p != node:
                self.transplant(sccsr, sccsr.right)
                sccsr.right = node.right
                sccsr.right.p = sccsr
            self.transplant(node, sccsr)
            sccsr.left = node.left
            sccsr.left.p = sccsr
    
    def min(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def max(self, node):
        while node.right != None:
            node = node.right
        return node

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.key, ", ")
            self.inorder(node.right)
            
if __name__ == "__main__":
    a = list(np.random.randint(0, 10, 10))
    a = [2, 4, 1, 0, 1, 7, 1, 3, 6, 4]
    print(a)
    t = BinarySearchTree(a)
    t.inorder(t.root)
    # t.transplant(t.search(1), t.search(4))
    t.delete(t.search(2))
    print("test")
    t.inorder(t.root)
    pass
