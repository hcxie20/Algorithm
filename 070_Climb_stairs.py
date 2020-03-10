# chose from go up 1 or 2
# -> you on n, you need to come from n-1 or n-2 ->
# f(n) = f(n-1) + f(n-2)

class Solution:
    def climbStairs(self, n):
        return self.getFibN(n)

    @staticmethod    
    def getFibN(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            pVal = 2
            ppVal = 1
            while n - 2 > 0:
                val = pVal + ppVal
                ppVal = pVal
                pVal = val
                n -= 1
            return pVal