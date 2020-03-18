# class Solution(object):
#   def findSubstring(self, s):
#     rst = 0
#     for i in range(len(s)):
#       for k in range(1, i + 1):
#         a = sum(int(x) for x in s[i - k:i])
#         b = sum(int(y) for y in s[i:i+k])
#         if sum(int(x) for x in s[i - k:i]) == sum(int(y) for y in s[i:i+k]):
#           rst = max(rst, k)
          
#     return 2 * rst
# print(Solution().findSubstring("1538023"))

# print(ord("b") - ord("a"))

# a = [1, 1, 2]
# b = set(a)
# print(b)
# a = 12
# # a = a >> 1
# a = a or 0
# print(a)

# class Solution(object):
# 	def powerTwo(self, num):
# 		while num != 0:
# 			num, remainder = divmod(num, 2)
#           if remainder != 0:
# 				    return False
#         return True

# a = 8
# b = 0x1000
# print(a & b)

import sys 
for line in sys.stdin:
    s = line
    seen = {}
    
    p1 = p2 = 0
    while p2 < len(s):      
        if s[p2] not in seen:
            s[p1] = s[p2]
            seen[s[p2]] = p2
            p1 += 1
        p2 += 1
    print(s[:p1])
