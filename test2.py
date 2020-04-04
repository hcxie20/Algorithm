# class Solution(object):
#     def find(self, ls):
#         length = len(ls)
#         rst = float("inf")
        
#         def oneStep(ls, i, num):
#             if not i < length - 1:
#                 return num

#             if ls[i] == 0:
#                 return oneStep(ls, i+1, num)
            
#             rst = float("inf")
            
#             if i <= length - 3 and ls[i] >= 2 and ls[i+1] >= 2 and ls[i+2] >= 2:
#                 newList = ls[:]
#                 newList[i] -= 2
#                 newList[i+1] -= 2
#                 newList[i+2] -= 2
#                 if newList[i] == 0:
#                     rst =  min(rst, oneStep(newList, i + 1, num + 1))
#                 else:
#                     rst = min(rst, oneStep(newList, i, num + 1))
                    
#             if i <= length - 5 and ls[i] >= 1 and ls[i+1] >= 1 and ls[i+2] >= 1 and ls[i+3] >= 1 and ls[i+4] >= 1:
#                 newList = ls[:]
#                 newList[i] -= 1
#                 newList[i+1] -= 1
#                 newList[i+2] -= 1
#                 newList[i+3] -= 1
#                 newList[i+4] -= 1
#                 if newList[i] == 0:
#                     rst = min(rst, oneStep(newList, i + 1, num + 1))
#                 else:
#                     rst = min(rst, oneStep(newList, i, num + 1))
                    
#             if ls[i] >= 2:
#                 newList = ls[:]
#                 newList[i] -= 2
#                 if newList[i] == 0:
#                     rst = min(rst, oneStep(newList, i + 1, num + 1))
#                 else:
#                     rst = min(rst, oneStep(newList, i, num + 1))
            
#             if ls[i] >= 1:
#                 newList = ls[:]
#                 newList[i] -= 1
#                 rst = min(rst, oneStep(newList, i + 1, num + 1))
            
#             return rst
        
#         rst = oneStep(ls, 0, 0)
#         print(rst)

# ls = [1, 1, 1, 2, 2, 2, 2, 2, 1, 1]
# Solution().find(ls)

class Solution:
    def find(self, length, ls):
        #print(length, ls)
        ls.sort(key=lambda x: x[0])
        self.rst = ""
        
        def oneStep(i, combo):
            if not i < length:
                if not self.rst:
                    self.rst = combo
                else:
                    if len(combo) > len(self.rst):
                        self.rst = combo
                return 
            
            if not combo:
                oneStep(i + 1, combo)
                oneStep(i + 1, combo + ls[i])
            else:
                if ord(ls[i][0]) >= ord(combo[-1]):
                    oneStep(i+1, combo+ls[i])
                oneStep(i+1, combo)
        
        oneStep(0, "")
        print(self.rst)

ls = [
    "aaa",
    "bcd",
    "zzz",
    "bcdef"
]
Solution().find(4, ls)