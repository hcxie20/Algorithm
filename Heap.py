'''
Mistakes: 
    1. the return for math.floor() is a float instead of a int
    2. range [) !!!!!
'''
import math
import numpy as np

class Heap:
    def __init__(self, ls):
        self.value = ["NULL"] + ls
        self.heapsize = len(ls)
        self.build_max_heap()

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l <= self.heapsize and self.value[largest] < self.value[l]:
            largest = l
        if r <= self.heapsize and self.value[largest] < self.value[r]:
            largest = r
        if largest != i:
            tmp = self.value[largest]
            self.value[largest] = self.value[i]
            self.value[i] = tmp
            self.max_heapify(largest)
    
    def build_max_heap(self):
        for i in range(int(math.floor(self.heapsize/2)), 0, -1):
            self.max_heapify(i)

    def sort(self):
        for i in range(self.heapsize, 1, -1):
            tmp = self.value[i]
            self.value[i] = self.value[1]
            self.value[1] = tmp
            self.heapsize -= 1
            self.max_heapify(1)
        return self

    @staticmethod
    def left(i):
        return 2 * i

    @staticmethod
    def right(i):
        return 2 * i + 1

    @staticmethod
    def parent(i):
        return math.floor(i/2)

if __name__ == "__main__":
    a = list(np.random.randint(0, 10, 10))
    a = [7, 2, 3, 6, 8, 9, 6, 6, 3, 2]
    print(a)
    b = Heap(a)
    print(b.value)
    print(b.sort().value)
    pass
