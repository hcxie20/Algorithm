import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # chose m-1 from m - 1 + n - 1
        return int((math.factorial(m + n - 2)) / ((math.factorial(n - 1)) * math.factorial(m - 1)))