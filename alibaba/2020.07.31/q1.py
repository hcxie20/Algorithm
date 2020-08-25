def min_path(map, src, dst):
    if not map:
        return 0

    _map = [x[:] for x in map]

    m = len(_map)
    n = len(_map[0])

    start_index = [src[0] - 1, src[1] - 1]
    end_index = [dst[0] - 1, dst[1] - 1]

    if start_index[0] < end_index[0] and start_index[1] < end_index[1]:
        pass

    elif start_index[0] < end_index[0] and start_index[1] > end_index[1]:
        for i in range(len(_map)):
            _map[i].reverse()

        start_index[1] = n - 1 - start_index[1]
        end_index[1] = n - 1 - end_index[1]


    elif start_index[0] > end_index[0] and start_index[1] < end_index[1]:
        _map.reverse()

        start_index[0] = m - 1 - start_index[0]
        end_index[0] = m - 1 - end_index[0]

    else:
        for i in range(len(_map)):
            _map[i].reverse()

        _map.reverse()

        start_index[1] = n - 1 - start_index[1]
        end_index[1] = n - 1 - end_index[1]
        start_index[0] = m - 1 - start_index[0]
        end_index[0] = m - 1 - end_index[0]

    dp = [[0 for _ in range(n)] for _ in range(m)]

    def cal_cost(src, dst):
        if _map[src[0]][src[1]] == 'C' and _map[dst[0]][dst[1]] == 'C':
            return 3

        elif _map[src[0]][src[1]] == 'C' and _map[dst[0]][dst[1]] == 'S':
            return 5

        elif _map[src[0]][src[1]] == 'S' and _map[dst[0]][dst[1]] == 'S':
            return 2

        else:
            return 5

    for i in range(start_index[0], end_index[0] + 1):
        for j in range(start_index[1], end_index[1] + 1):
            if i == start_index[0] and j == start_index[1]:
                continue

            elif i == start_index[0]:
                dp[i][j] = dp[i][j - 1] + cal_cost([i, j - 1], [i, j])

            elif j == start_index[1]:
                dp[i][j] = dp[i - 1][j] + cal_cost([i - 1, j], [i, j])

            else:
                dp[i][j] = min(
                    dp[i][j - 1] + cal_cost([i, j - 1], [i, j]),
                    dp[i - 1][j] + cal_cost([i - 1, j], [i, j])
                )

    return dp[end_index[0]][end_index[1]]



if __name__ == '__main__':
    map = [
        ['C', 'C', 'C', 'S'],
        ['S', 'S', 'S', 'S'],
        ['C', 'S', 'C', 'S'],
        ['S', 'S', 'C', 'C']
    ]
    start = [1, 1]
    end = [3, 4]
    print(min_path(map, start, end))

    start = [3, 1]
    end = [1, 3]
    print(min_path(map, start, end))

    start = [1, 2]
    end = [2, 1]
    print(min_path(map, start, end))

    start = [2, 2]
    end = [1, 1]
    print(min_path(map, start, end))
