'''
Find the max subarray

Question: buy and sell stock, find the highest profit with given price chart
    Buy with lowest and sell with highest price. X
    -> Find the Differen of the price chart. The Max Sum would be the highest profit.

Solution: divide-and-conquer
    Given a list A, and the low and high indice, find the max subarray
    Set mid = floor((low + high)/2)
    The max subarray can only lie in
        - A[low, mid]
        - A[mid + 1, high] ************ important: mid + 1
        - A[low, high], and CROSS the mid indice
    The reason for such divide is that there is simple way to calculate case iii, with \Theta(n):
        for i = mid to low, define a sum. Plus all A[i]s and find the max sum. The same goes for mid + 1 to high. We find the max crossing subarray.
    For case i and ii:
        If low == high, means that there is only one element. It MUST be the max subarray;
        Else, divide them to two subarray, run each subarray with new indices.
    And compare the max sum for all three cases, we find the max subarray.

    T(n) = 2T(n/2) + \theta(n)

Mistakes:
    1. When using np.floor(), the return is a np.float64, which CANNOT be used for indices.
    2. The correct indice for the right subarray is A[mid + 1, high], not A[mid, high]
    3. About function range():
        - Three args: start, stop and stride
        - The built-in start point is 0. 
        - Generate a list from start to end, WITHOUT end.
            e.g.: 
                - range(5) -> 0, 1, 2, 3, 4
        - Stride is REQUIRED when start > stop 
            e.g.:
                - range(5, 0) -> NOTHING HAPPENDS
                - range(5, 0, -1) -> 5, 4, 3, 2, 1
    4. a = np.array([0, 1, 2, 3, 4])
        a.size = 5

'''

import numpy as np


def find_max_subarray(_list, low, high):
    if low == high:
        return low, high, _list[low]
    else:
        mid = int(np.floor((low + high)/2, dtype=float)) # !!!!!!!!!!!!!!!!!!!!!!!!!
        left_low, left_high, left_sum = find_max_subarray(_list, low, mid)
        right_low, right_high, right_sum = find_max_subarray(_list, mid + 1, high) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        x_low, x_high, x_sum = find_max_xing_subarray(_list, low, mid, high)
        
        if left_sum >= right_sum and left_sum >= x_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= x_sum:
            return right_low, right_high, right_sum
        else:
            return x_low, x_high, x_sum
    pass

def find_max_xing_subarray(_list, low, mid, high):
    sum = 0
    left_max = mid
    left_sum = -float("inf")
    for i in range(mid, low - 1, -1): # !!!!!!!!!!!!!!!!!!!!!!!
        sum += _list[i]
        if sum > left_sum:
            left_sum = sum
            left_max = i
    sum = 0
    right_max = mid + 1
    right_sum = -float("inf")
    for i in range(mid + 1, high + 1):# !!!!!!!!!!!!!!!!!!!!!!!
        sum += _list[i]
        if sum > right_sum:
            right_sum = sum
            right_max = i
    return left_max, right_max, left_sum + right_sum


if __name__ == "__main__":
    a = np.random.randint(low=-20, high=20, size=10)
    print(a)
    left, right, sum = find_max_subarray(a, 0, a.size - 1) # !!!!!!!!!!!!!!!
    print(left, "\n", right, "\n", sum)
