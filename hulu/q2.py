class Solution():
    def find_max(self, m, n, ls):
        if not ls:
            return 0

        rst = float('-inf')

        def find_u(i, j):
            rst = float('inf')

            for k in range(n):
                rst = min(rst, max(ls[i][k], ls[j][k]))

            return rst

        dp = [[0 for _ in range(m)] for _ in range(m)]

        for i in range(m):
            dp[i][i] = find_u(i, i)
            rst = max(rst, dp[i][i])

        for length in (1, m - 1):
            for i in range(m - 1 - length):
                for j in range(n):
                    dp[i][j] = max(find_u(i, j), dp[i][j - 1], dp[i + 1][j])

        return rst


if __name__ == '__main__':
    ls = [
        [5, 0, 3, 1, 2],
        [1, 8, 9, 1, 3],
        [1, 2, 3, 4, 5],
        [9, 1, 0, 3, 7],
        [2, 3, 0, 6, 3],
        [6, 4, 1, 7, 0]
    ]
    print(Solution().find_max(6, 5, ls))

    ls = [
        [1, 2, 3, 4, 5]
    ]
    print(Solution().find_max(len(ls), len(ls[0]), ls))
