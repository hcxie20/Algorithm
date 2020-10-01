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

        # parts = []
        # for fence in ls:
        #     if fence[1] < k:
        #         parts.append((fence[0], fence[1]))
        #     else:
        #         parts.append((fence[0], k))

        pass
        return x_axis
        # 计算各个区间有多少种走法
        # 。。。


if __name__ == '__main__':
    ls = [
        [0, 2, 3],
        [2, 3, 4],
        [3, 4, 0],
        [4, 6, 1]
    ]
    print(Solution().find_paths(4, 5, ls))
