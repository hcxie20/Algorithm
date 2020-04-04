class Solution(object):
    def removeDuplicate(self, s):
        ls = [None] + list(s)

        p1 = p2 = 1
        end = len(ls)
        flag = True

        while flag:
            flag = False
            while p2 < end:
                if ls[p2] != ls[p2-1]:
                    ls[p1] = ls[p2]
                    p1 += 1
                else:
                    p1 -= 1
                    flag = True
                p2 += 1
            end = p1
            p1 = p2 = 1
        return "".join(ls[1:end])


s = "ACCCA"
rst = Solution().removeDuplicate(s)
print(rst)
