class Solution:
    def combinationSum(self, candidates, target: int):
        if not candidates:
            return []

        candidates.sort(reverse=True)
        rst = []

        def backtrack(candidates, i, target, cur):
            if target == 0:
                rst.append(cur)
                return

            if i == len(candidates):
                return

            for k in range(0, target // candidates[i] + 1):
                backtrack(candidates, i + 1, target - k * candidates[i], cur + [candidates[i]] * k)

        backtrack(candidates, 0, target, [])

        return rst


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
