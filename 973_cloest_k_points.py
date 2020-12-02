class Solution:
    def kClosest(self, points, K: int):

        def distance(point):
            return (point[0] ** 2 + point[1] ** 2) ** 0.5

        def quick_select(i, j, k):
            pivot_index = i
            pivot = distance(points[j])

            for p in range(i, j):
                if distance(points[p]) <= pivot:
                    points[pivot_index], points[p] = points[p], points[pivot_index]
                    pivot_index += 1

            points[pivot_index], points[j] = points[j], points[pivot_index]

            if pivot_index - i + 1 == k:
                return

            elif pivot_index - i + 1 > k:
                quick_select(i, pivot_index - 1, k)
            else:
                quick_select(pivot_index + 1, j, k - (pivot_index - i + 1))

        quick_select(0, len(points) - 1, K)
        print(points)
        return points[:K]


if __name__ == '__main__':
    import random
    p = [[1, 0], [3, 0], [4, 0], [5, 0], [2, 0]]
    random.shuffle(p)
    print(p)
    print(Solution().kClosest(p, 1))
