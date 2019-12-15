class Solution(object):
    def __init__(self, str1, str2):
        self.value = 0
        self.str = ""
        if str1 and str2:
            dp = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
            for i in range(1, len(str2) + 1):
                for j in range(1, len(str1) + 1):
                    if str1[j - 1] == str2[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            while i != 0:
                if dp[i][j] == dp[i - 1][j - 1]:
                    self.str = str2[i - 1] + self.str
                    i -= 1
                    j -= 1
                elif dp[i][j] == dp[i - 1][j]:
                    i -= 1
                else:
                    j -= 1
        pass


if __name__ == "__main__":
    a = "abcdef"
    b = ""
    c = Solution(a, b)