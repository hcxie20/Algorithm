class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        pre_dict = {}
        status = [0] * numCourses

        for require in prerequisites:
            if require[0] in pre_dict:
                pre_dict[require[0]].append(require[1])
            else:
                pre_dict[require[0]] = [require[1]]

        rst = []
        flag = True

        def dfs(course):
            nonlocal rst, flag
            if course not in pre_dict:
                rst.append(course)
                status[course] = 2
                return
            
            status[course] = 1

            for pre in pre_dict[course]:
                if flag is False:
                    return
                elif status[pre] == 1:
                    flag = False
                elif status[pre] == 2:
                    continue
                else:
                    dfs(pre)
            
            rst.append(course)
            status[course] = 2

        for course in range(numCourses):
            if status[course] == 0:
                dfs(course)

        if flag:
            return rst
        else:
            return []


if __name__ == '__main__':
    print(Solution().findOrder(2, [[0, 1]]))              
    print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))              
    print(Solution().findOrder(2, [[1,0], [0, 1]]))              
