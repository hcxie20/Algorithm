import math
class Solution:
    def expect(self , n ):
        rst = 0

        def c(n, k):
            # return tmp(n, k) / math.factorial(k)
            return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))

        def tmp(n, k):
            rst = 1
            tmp = n
            while tmp >= n - k:
                rst *= tmp
                tmp -= 1
            return rst

        for k in range(n):
            a = c(n + k, k) * (0.5 ** (n + k)) * (n - k)
            rst += a


        return rst


if __name__ == '__main__':
    print(Solution().expect(2))
