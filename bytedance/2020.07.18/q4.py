def magic_stick(image, point_click):
    if not image:
        return

    color = image[point_click[0]][point_click[1]]
    m = len(image)
    n = len(image[0])

    rst = []
    rst.append(point_click)
    stack = []
    stack.append([point_click[0], point_click[1]])
    image[point_click[0]][point_click[1]] = 1 - color

    def find_neighbors(point):
        x, y = point[0], point[1]
        rst = []

        if x != 0:
            rst.append([x - 1, y])
        if x != m - 1:
            rst.append([x + 1, y])
        if y != 0:
            rst.append([x, y - 1])
        if y != n - 1:
            rst.append([x, y + 1])
        return rst

    # visited = []

    while stack:
        point = stack.pop()
        # visited.append(point)

        for neighbor in find_neighbors(point):
            if image[neighbor[0]][neighbor[1]] == color:
                if neighbor not in rst:
                    rst.append(neighbor)
                stack.append(neighbor)
                image[neighbor[0]][neighbor[1]] = 1 - color

    rst.sort(key=lambda x: (x[0], x[1]))
    return rst


if __name__ == '__main__':
    # 注意点击坐标（列，行）
    image = [[1, 0, 1], [0, 1, 1]]
    point = [1, 2]
    rst = magic_stick(image, point)
    for point in rst:
        print('({0},{1})'.format(point[0], point[1]), end='')
    print('\n')

    image = [[1, 1, 1], [1, 1, 1], [1, 0, 1]]
    point = [0, 0]
    print(magic_stick(image, point))

