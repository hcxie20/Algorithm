class Solution:

    def getMinScore(self , gz ):
        rst = float('inf')

        def recur(ls, score=0):
            nonlocal rst
            if score > rst:
                return

            if len(ls) == 1:
                rst = min(score, rst)
                return

            if len(ls) == 2:
                rst = min(score + ls[0] + ls[1], rst)
                return

            recur([ls[0] + ls[1]] + ls[2:], score=score + ls[0] + ls[1])
            if len(ls) > 3:
                recur([ls[0]] + [ls[1] + ls[2]] + ls[3:], score=score + ls[1] + ls[2])
            else:
                recur([ls[0]] + [ls[1] + ls[2]], score=score + ls[1] + ls[2])

        recur(gz, score=0)
        return rst


if __name__ == '__main__':
    # print(Solution().getMinScore([1, 3, 5, 2, 4]))
    # print(Solution().getMinScore([1]))
    print(Solution().getMinScore([1, 2, 3]))
