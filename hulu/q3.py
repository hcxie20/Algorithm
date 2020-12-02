class Solution():
    def find_paths(self, n, k, ls):
        x_axis = [float('inf') for _ in range(k + 1)]
        x_axis[0] = 0
        x_axis[k] = 0

        for fence in ls:
            for x in range(fence[0], fence[1] + 1):
                if x < k:
                    x_axis[x] = min(fence[2], x_axis[x])

        for i in range(k):
            if x_axis[i] + 1 < x_axis[i + 1]:
                x_axis[i + 1] = x_axis[i] + 1

        for i in range(k, -1, -1):
            if x_axis[i] + 1 < x_axis[i - 1]:
                x_axis[i - 1] = x_axis[i] + 1

        print(x_axis)
        # 计算各个区间有多少种走法

        dp = [[0 for _ in range(len(x_axis))] for _ in range(len(x_axis))]
        dp[0][0] = 1

        for i in range(1, len(x_axis)):
            for j in range(x_axis[i] + 1):
                left_up = 0
                left = 0
                left_down = 0

                if 0 <= j - 1 <= x_axis[i - 1]:
                    left_down = dp[i - 1][j - 1]

                if 0 <= j <= x_axis[i - 1]:
                    left = dp[i - 1][j]

                if 0 <= j + 1 <= x_axis[i - 1]:
                    left_up = dp[i - 1][j + 1]

                dp[i][j] = left_up + left + left_down

        print(dp)
        return dp[len(x_axis) - 1][0]


if __name__ == '__main__':
    ls = [
        [0, 2, 3],
        [2, 3, 4],
        [3, 4, 0],
        [4, 6, 1]
    ]
    print(Solution().find_paths(4, 5, ls))
