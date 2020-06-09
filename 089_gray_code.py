class Solution:
    def grayCode(self, n: int):
        if n == 0:
            return [0]

        rst = ["0", "1"]

        for _ in range(2, n + 1):
            tmp = ["1" + x for x in rst]
            rst = ["0" + x for x in rst]
            tmp.reverse()
            rst += tmp

        rst_value = [self.cal(x) for x in rst]
        return rst_value

    @staticmethod
    def cal(s):
        rst = 0
        n = len(s) - 1
        for c in s:
            rst += 2 ** n * int(c)
            n -= 1

        return rst

