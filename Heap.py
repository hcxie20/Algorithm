'''
Mistakes:
    1. the return for math.floor() is a float instead of a int
    2. range [) !!!!!
'''
import math

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

    def pop(self):
        self.value[1], self.value[self.heapsize] = self.value[self.heapsize], self.value[1]
        popitem = self.value.pop()
        self.heapsize -= 1
        self.max_heapify(1)
        return popitem

    def push(self, num):
        self.value.append(num)
        self.heapsize += 1
        self.value[1], self.value[self.heapsize] = self.value[self.heapsize], self.value[1]
        self.max_heapify(1)

    @staticmethod
    def left(i):
        return 2 * i

    @staticmethod
    def right(i):
        return 2 * i + 1

    @staticmethod
    def parent(i):
        return math.floor(i / 2)
    


class HeapNew(object):
    def __init__(self, ls):
        self.value = ls[:]
        self.heap_size = len(ls)
        self.build_heap()

    @staticmethod
    def find_left(index):
        return 2 * index + 1

    @staticmethod
    def find_right(index):
        return 2 * index + 2

    def max_heapify(self, i):
        l = self.find_left(i)
        r = self.find_right(i)

        largest = i

        if l < self.heap_size and self.value[largest] < self.value[l]:
            largest = l

        if r < self.heap_size and self.value[largest] < self.value[r]:
            largest = r

        if largest != i:
            self.value[i], self.value[largest] = self.value[largest], self.value[i]
            self.max_heapify(largest)

    def build_heap(self):
        for i in range(self.heap_size // 2, -1, -1):
            self.max_heapify(i)

    def pop(self):
        self.value[0], self.value[-1] = self.value[-1], self.value[0]
        rst = self.value.pop()
        self.heap_size -= 1

        self.max_heapify(0)
        return rst

    def sort(self):
        for i in range(self.heap_size, 0, -1):
            self.value[i], self.value[0] = self.value[0], self.value[i]
            self.max_heapify(0)


class Finder:
    def findKth(self, a, n, K):
        # write code here
        heap = Heap(a)

        for _ in range(K):
            rst = heap.pop()

        return rst

if __name__ == "__main__":
    # a = list(np.random.randint(0, 10, 10))
    a = [7, 2, 3, 6, 8, 9, 6, 6, 3, 2]
    print(a)
    b = HeapNew(a)
    print(b.value)
    # print(b.sort().value)
    ls = []
    for i in range(3):
        ls.append(b.pop())
    print(ls)
    # print(b.value)
    # b.push(5)
    # print(b.value)
    # b.push(3)
    # print(b.value)

    # b.push(9)
    # print(b.value)

    pass
