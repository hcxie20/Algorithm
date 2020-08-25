from collections import defaultdict

'''
BFS from leave nodes to center
'''

class Solution:
    def findMinHeightTrees(self, n, edges):
        degree_ls = [0] * n
        neighbor_dict = defaultdict(list)

        if n <= 2:
            return list(range(n))

        for edge in edges:
            degree_ls[edge[0]] += 1
            degree_ls[edge[1]] += 1
            neighbor_dict[edge[0]].append(edge[1])
            neighbor_dict[edge[1]].append(edge[0])

        queue = []

        for i in range(len(degree_ls)):
            if degree_ls[i] == 1:
                queue.append(i)
                degree_ls[i] -= 1

        while True:
            node_ls = queue[:]
            queue = []

            for node in node_ls:
                assert len(neighbor_dict[node]) == 1
                neighbor = neighbor_dict.pop(node)[0]
                neighbor_dict[neighbor].remove(node)
                degree_ls[neighbor] -= 1

            if len(neighbor_dict.keys()) <= 2:
                break

            for i in range(len(degree_ls)):
                if degree_ls[i] == 1:
                    queue.append(i)
                    degree_ls[i] -= 1
        
        return [key for key in neighbor_dict.keys()]


if __name__ == '__main__':
    print(Solution().findMinHeightTrees(2, [[1, 0], [1, 2], [1, 3]]))
    print(Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    print(Solution().findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))
