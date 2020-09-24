# # # class Solution(object):
# # #   def findSubstring(self, s):
# # #     rst = 0
# # #     for i in range(len(s)):
# # #       for k in range(1, i + 1):
# # #         a = sum(int(x) for x in s[i - k:i])
# # #         b = sum(int(y) for y in s[i:i+k])
# # #         if sum(int(x) for x in s[i - k:i]) == sum(int(y) for y in s[i:i+k]):
# # #           rst = max(rst, k)
          
# # #     return 2 * rst
# # # print(Solution().findSubstring("1538023"))

# # # print(ord("b") - ord("a"))

# # # a = [1, 1, 2]
# # # b = set(a)
# # # print(b)
# # # a = 12
# # # # a = a >> 1
# # # a = a or 0
# # # print(a)

# # # class Solution(object):
# # # 	def powerTwo(self, num):
# # # 		while num != 0:
# # # 			num, remainder = divmod(num, 2)
# # #           if remainder != 0:
# # # 				    return False
# # #         return True

# # # a = 8
# # # b = 0x1000
# # # print(a & b)

# # import sys 
# # for line in sys.stdin:
# #     s = line
# #     seen = {}
    
# #     p1 = p2 = 0
# #     while p2 < len(s):      
# #         if s[p2] not in seen:
# #             s[p1] = s[p2]
# #             seen[s[p2]] = p2
# #             p1 += 1
# #         p2 += 1
# #     print(s[:p1])



# a = 1
# b = 2
# c = 255

# def findIP(ip, mask):
#         num1 = ip.split(".")
#         num2 = mask.split(".")
#         rst = ""
#         for i in range(4):
#             rst += str((int(num1[i]) & int(num2[i])))
#             rst += "."
#         return rst[:-1]
# e = findIP("192.168.2.1", "255.255.255.255")
# print(a & c, b & c)


# class Solution(object):
#     def __init__(self, grid, length):
        
#         def find(nodes, level):
#             newNodes = []
#             for node in nodes:
#                 if grid[node[0]][node[1]] != 0:
#                     return level
                
#                 # add next level
#                 for direction in [[0, 1], [1, 0], [1, 1]]:
#                     i, j = node[0] + direction[0], node[1] + direction[1]
#                     if 0 <= i < length and 0 <= j < length:
#                         if [i, j] not in nodes and [i, j] in newNodes:
#                             newNodes.append([i, j])
                            
#             if not newNodes:
#                 return level
#             return find(newNodes, level + 1)


#         rst = 0
#         #print(grid)
#         for i in range(length):
#             for j in range(length):
#                 rst = max(rst, find([[i, j]], 0))
#         print(rst ** 2)



# class treeNode:
#   def __init__(self, a, b):
# 	self.a = a
#     self.b = b
#     self.left = None
#     self.right = None

# def construct(ls):
#   if not ls:
#     return None
  
#   def insertNode(cur, target):
#     if target.a <= cur.a:
#       if cur.left == None:
#         cur.left = target
#       else:
#         insertNode(cur.left, target)
    
#     else:
#       if cur.right == None:
#         cur.right = target
#       else:
#         insertNode(cur.right, target)
  
#   ls.sort(key=lambda x: x[1])
  
#   root = treeNode(ls[0][0], ls[0][1])
  
#   for i in range(1, len(ls)):
#     newNode = treeNode(ls[i][0], ls[i][1])
#     insertNode(root, newNode)  
  
#   return root


import re

obj = re.match('', 'dog')
if re.match(r'a', 'dog'):
    print('dog')

from functools import lru_cache
from cachetools import cached, TTLCache

# @cached(cache=TTLCache(maxsize=128, ttl=600))

@lru_cache()
def test(a=1, b=2):
    return a, b


test()
# test([1, 2, 3], b=2)

class ClassA(object):
    def __init__(self):
        self.__data = {}

    def print(self):
        print(self.__data)

class ClassB(ClassA):
    def __init__(self):
        ClassA.__init__(self)

    def print(self):
        print(self.__data)

# class ClassC(ClassA):
#     def __init__(self):
#         super(ClassC, self).__init__()

#     def print(self):
#         print(self._ClassA__data)


# # obj = ClassB()
# # obj.print()

# obj_c = ClassC()
# print(dir(obj_c))
# obj_c.print()
# pass

# class C(list):

#     __slots__ = 'hashed_value'

#     def __init__(self, tup):
#         self[:] = tup
#         self.hashed_value = hash(tup)

#     def __hash__(self):
#         return self.hashed_value


if __name__ == '__main__':
    a = ClassA()
    print(a.print.__name__)
    b = ClassA()
    print(b.print.__name__)
    pass
