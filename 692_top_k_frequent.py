import heapq

class Solution:
    def topKFrequent(self, words, k):
        seen_dict = {}
        heap = MinHeap(k)

        for word in words:
            if word not in seen_dict:
                seen_dict[word] = 1
            else:
                seen_dict[word] += 1

        for key, value in seen_dict.items():
            word = Word(key, value)
            heap.insert(word)

        heap.sort()
        rst = []
        for word in heap.data:
            rst.append(word.word)

        return rst

class Word(object):
    def __init__(self, word, freq):
        self._word = word
        self._freq = freq

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{0}: {1}'.format(self._word, self._freq)

    @property
    def word(self):
        return self._word

    @property
    def freq(self):
        return self._freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        else:
            return self.freq < other.freq

class MinHeap(object):
    def __init__(self, depth):
        self._max_depth = depth
        self._depth = 0
        self._data = [None] * depth

    @property
    def data(self):
        return self._data[:self._depth]

    def top(self):
        return self._data[0] if self._depth > 0 else None

    def left(self, i):
        tmp = 2 * i + 1
        return tmp if tmp < self._depth else None

    def right(self, i):
        tmp = 2 * i + 2
        return tmp if tmp < self._depth else None

    def parrent(self, i):
        tmp = (i - 1) // 2
        return tmp if tmp >= 0 else None

    def min_heapify(self, index):
        min_index = index

        l_index = self.left(index)
        r_index = self.right(index)

        if l_index and self._data[l_index] < self._data[min_index]:
            min_index = l_index

        if r_index and self._data[r_index] < self._data[min_index]:
            min_index = r_index

        if min_index != index:
            self._data[min_index], self._data[index] = self._data[index], self._data[min_index]
            self.min_heapify(min_index)

    def heapify(self):
        for i in range(self._depth // 2, 0, -1):
            self.min_heapify(i)

    def _insert_tail(self, val):
        self._data[self._depth] = val
        self._depth += 1

        tmp = self._depth - 1
        p_index = self.parrent(tmp)

        while p_index is not None and not self._data[p_index] < val:
            self._data[p_index], self._data[tmp] = self._data[tmp], self._data[p_index]
            tmp = p_index
            p_index = self.parrent(p_index)

    def insert(self, val):
        if self._depth == 0:
            self._depth += 1
            self._data[0] = val
            return

        if self._depth < self._max_depth:
            self._insert_tail(val)

        elif not val < self.top():
            self._data[0] = val
            self.min_heapify(0)

    def sort(self):
        tmp = self._depth
        for i in range(self._depth - 1, 0, -1):
            self._data[0], self._data[i] = self._data[i], self._data[0]
            self._depth -= 1
            self.min_heapify(0)

        self._depth = tmp


if __name__ == '__main__':
    ls = ['a', 'a', 'b']
    print(Solution().topKFrequent(ls, 2))

    ls = ["i", "love", "leetcode", "i", "love", "coding"]
    print(Solution().topKFrequent(ls, 2))

    ls = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    print(Solution().topKFrequent(ls, 4))
    print(Solution().topKFrequent(ls, 1))
    print(Solution().topKFrequent(ls, 2))

    ls = ['a', 'b', 'c']
    print(Solution().topKFrequent(ls, 3))

    ls = ["glarko","zlfiwwb","nsfspyox","pwqvwmlgri","qggx","qrkgmliewc","zskaqzwo","zskaqzwo","ijy","htpvnmozay","jqrlad","ccjel","qrkgmliewc","qkjzgws","fqizrrnmif","jqrlad","nbuorw","qrkgmliewc","htpvnmozay","nftk","glarko","hdemkfr","axyak","hdemkfr","nsfspyox","nsfspyox","qrkgmliewc","nftk","nftk","ccjel","qrkgmliewc","ocgjsu","ijy","glarko","nbuorw","nsfspyox","qkjzgws","qkjzgws","fqizrrnmif","pwqvwmlgri","nftk","qrkgmliewc","jqrlad","nftk","zskaqzwo","glarko","nsfspyox","zlfiwwb","hwlvqgkdbo","htpvnmozay","nsfspyox","zskaqzwo","htpvnmozay","zskaqzwo","nbuorw","qkjzgws","zlfiwwb","pwqvwmlgri","zskaqzwo","qengse","glarko","qkjzgws","pwqvwmlgri","fqizrrnmif","nbuorw","nftk","ijy","hdemkfr","nftk","qkjzgws","jqrlad","nftk","ccjel","qggx","ijy","qengse","nftk","htpvnmozay","qengse","eonrg","qengse","fqizrrnmif","hwlvqgkdbo","qengse","qengse","qggx","qkjzgws","qggx","pwqvwmlgri","htpvnmozay","qrkgmliewc","qengse","fqizrrnmif","qkjzgws","qengse","nftk","htpvnmozay","qggx","zlfiwwb","bwp","ocgjsu","qrkgmliewc","ccjel","hdemkfr","nsfspyox","hdemkfr","qggx","zlfiwwb","nsfspyox","ijy","qkjzgws","fqizrrnmif","qkjzgws","qrkgmliewc","glarko","hdemkfr","pwqvwmlgri"]
    print(Solution().topKFrequent(ls, 14))
