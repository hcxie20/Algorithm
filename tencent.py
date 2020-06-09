# import sys
# class queue(object):
#     def __init__(self):
#         self.ls = []
#         self.length = 0

#     def push(self, x):
#         self.ls.append(x)
#         self.length += 1

#     def pop(self):
#         if self.length == 0:
#             print(-1)
#             return -1

#         self.ls.pop(0)
#         self.length -= 1

#     def top(self):
#         if self.length == 0:
#             print(-1)
#             return -1

#         print(self.ls[0])

#     def size(self):
#         print(self.length)

#     def clear(self):
#         self.ls = []
#         self.length = 0





# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     console_in =
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         num = int(line)
#         ls = []
#         for j in range(num):
#             line = sys.stdin.readline().strip()
#             values = list(line.split())
#             ls.append(values)

#         q = queue()
#         for j in range(num):
#             #print(ls[j])
#             if ls[j][0] == 'PUSH':
#                 q.push(int(ls[j][1]))
#             elif ls[j][0] == 'POP':
#                 q.pop()
#             elif ls[j][0] == 'TOP':
#                 q.top()
#             elif ls[j][0] == 'SIZE':
#                 q.size()







# import sys

# def parent(x, k):
#     # find depth of x
#     d = 1
#     while x > 2 ** d - 1:
#         d += 1

#     if d <= k:
#         print(-1)
#         return -1

#     n = d - k
#     while n != 0:
#         x = x // 2
#         n -= 1
#     print(x)



# if __name__ == "__main__":
#     # 读取第一行的n
#     console_in = [
#         '10 1',
#         '10 2',
#         '10 3',
#         '10 4'
#     ]
#     n = 4
#     ls = []
#     for i in range(n):
#         # 读取每一行
#         line = console_in[i]
#         print(line)
#         # 把每一行的数字分隔后转化成int列表
#         values = list(line.split())
#         ls.append(values)
#     for i in range(n):
#         parent(int(ls[i][0]), int(ls[i][1]))

import math
import sys
import numpy as np
def find(ls1, ls2):
    array1 = np.array(ls1)
    array2 = np.array(ls2)
    d = list(array1 - array2)
    dis = [math.sqrt(x[0] ** 2 + x[1] ** 2) for x in d]
    print(min(dis))
    pass




if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())

    # for _ in range(n):
    #     ls = []
    #     lines = int(sys.stdin.readline().strip())
    #     for j in range(2 * lines):
    #         line = sys.stdin.readline().strip()
    #         values = list(line.split())
    #         values = [int(x) for x in values]
    #         ls.append(values)
    #     find(ls[:lines], ls[lines:])
    ls1 = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    ls2 = [
        [2, 2],
        [2, 3],
        [3, 2],
        [3, 2]
    ]
    find(ls1, ls2)
