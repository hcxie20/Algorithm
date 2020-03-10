class Solution:
    def reverse(self, x):
        stack = []
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        ls = list(str(x))
        for i in range(len(ls)):
            stack.append(ls[i])
        
        tmp = stack.pop()
        while not tmp:
            tmp = stack.pop()

        rstString = str(tmp)
        while stack:
            rstString += str(stack.pop())
        
        rst = sign * int(rstString)
        if rst > 2 ** 31 - 1 or rst < -2 ** 31:
            return 0
        else:
            return rst


class Solution2:
    def reverse(self, x):
        rst = 0
        r = 0 # remainder
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        while x != 0:
            x, r = divmod(x, 10)
            rst = rst * 10 + r
        
        if rst > 2 ** 31 - 1 or rst < -2 ** 31:
            return 0
        else:
            return sign * rst

print(Solution2().reverse(-123))
            
            
