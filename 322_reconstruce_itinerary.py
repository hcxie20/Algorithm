# https://leetcode-cn.com/problems/reconstruct-itinerary/solution/javadfsjie-fa-by-pwrliang/

import collections

class Solution:
    def findItinerary(self, tickets):
        rst = []

        fly_dict = collections.defaultdict(list)
        for tick in tickets:
            fly_dict[tick[0]].append(tick[1])

        for key in fly_dict.keys():
            fly_dict[key].sort()

        def dfs(node):
            if len(fly_dict[node]) == 0:
                rst.insert(0, node)
                return 

            while len(fly_dict[node]) != 0:
                next_node = fly_dict[node].pop(0)
                dfs(next_node)
            rst.insert(0, node)

        dfs('JFK')

        return rst


if __name__ == "__main__":
    print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
