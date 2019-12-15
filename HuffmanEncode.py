import numpy as np
import math


class Node:
    def __init__(self, name, freq):
        self.left = None
        self.right = None
        self.freq = freq
        self.name = name


class Huffman:
    def __init__(self, ls):
        '''
        ls: list of nodes
            freq
        '''
        self.heap = self.MinHeap(ls)
        tmp = self.heap
        for i in range(1, len(ls)):
            tmp_node = Node(None, None)
            tmp_node.left = node_left = tmp.extract_min()
            tmp_node.right = node_right = tmp.extract_min()
            tmp_node.freq = node_left.freq + node_right.freq
            tmp.insert(tmp_node)
        pass
        self.encoded = tmp

    class MinHeap:
        def __init__(self, ls):
            self.heap_size = len(ls)
            self.heap = ["None"] + ls
            for i in range(int(math.floor(self.heap_size/2)), 0, -1):
                self.heapify(i)

        def heapify(self, i):
            l = self.left(i) 
            r = self.right(i)
            mini = i
            if l <= self.heap_size and self.heap[l].freq < self.heap[mini].freq:
                mini = l
            if r <= self.heap_size and self.heap[r].freq < self.heap[mini].freq:
                mini = r
            if mini != i:
                self.heap[i], self.heap[mini] = self.heap[mini], self.heap[i]
                self.heapify(mini)
        
        def left(self, i):
            return 2 * i

        def right(self, i):
            return 2 * i + 1

        def parent(self, i):
            return int(math.floor(i/2))

        def extract_min(self):
            node = self.heap[1]
            self.heap[1] = self.heap[self.heap_size]
            self.heap_size -= 1
            self.heap.pop()
            self.heapify(1)
            return node

        def increase_key(self, i, key):
            self.heap[i].freq = key
            while i > 1 and self.heap[i].freq < self.heap[self.parent(i)].freq:
                self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                i = self.parent(i)

        def insert(self, node):
            self.heap_size += 1
            self.heap.append(node)
            self.increase_key(self.heap_size, node.freq)



if __name__ == "__main__":
    a = Node("a", 45)
    b = Node("b", 13)
    c = Node("c", 12)
    d = Node("d", 16)
    e = Node("e", 9)
    f = Node("f", 5)
    ls = [a, b, c, d, e, f]

    Huffman(ls)

    