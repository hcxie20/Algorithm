import numpy as np
import math


def QuickSort(ls, p, r):
    if p < r:
        q = sort(ls, p, r)
        QuickSort(ls, p, q-1)
        QuickSort(ls, q+1, r)
    return ls


def sort(ls, p, r):
    # all ls[i] <= x
    # pivot on i + 1
    x = ls[r]
    i = p - 1
    tmp = 0
    for j in range(p, r): # p to r-1
        if ls[j] <= x:
            i = i + 1
            tmp = ls[j]
            ls[j] = ls[i]
            ls[i] = tmp
    tmp = x
    ls[r] = ls[i + 1]
    ls[i + 1] = tmp
    return i + 1


if __name__ == "__main__":
    a = list(np.random.randint(0, 10, 10))
    a = [9, 9, 9, 3, 4, 5, 6]
    print(a)
    a = QuickSort(a, 0, len(a)-1)
    print(a)
