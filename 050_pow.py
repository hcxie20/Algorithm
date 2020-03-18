class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        def pow(x, n):
            if n == 0:
                return 1
                
            if n % 2 == 0:
                return pow(x, n/2) ** 2
            else:
                return x * pow(x, n//2) ** 2

        return pow(x, n)