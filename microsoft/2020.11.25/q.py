# 题目： 输入：[2, 3, 6, 9] 目标值9
# 输出：[9], [3,3,3], [3,6], [2,2,2,3]


class Solution(object):
    def findComb(self, src, target):
        if not src:
            return []

        self.rst = []
        src.sort(reverse=True)

        self.recursive(src, 0, target, [])
        return self.rst

    def recursive(self, src, cur_src_id, target, cur_rst):
        if target == 0:
            self.rst.append(cur_rst)
            return

        if cur_src_id >= len(src):
            return

        k = target // src[cur_src_id]

        tmp = src[cur_src_id]
        new_src_id = cur_src_id
        while new_src_id < len(src) and tmp == src[new_src_id]:
            new_src_id += 1

        for i in range(k + 1):
            self.recursive(src, cur_src_id + 1, target - i * src[cur_src_id], cur_rst + [src[cur_src_id]] * i)


if __name__ == '__main__':
    src = [2, 3, 3, 6, 9]
    target = 9
    print(Solution().findComb(src, target))
