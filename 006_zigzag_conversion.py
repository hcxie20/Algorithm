class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rst = ["" for _ in range(numRows)]
        i = 0
        flag = -1 # !!!!!

        for word in s:
            rst[i] += word
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag

        return "".join(rst)