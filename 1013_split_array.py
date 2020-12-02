class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        pre = [0] * (len(A) + 1)
        for i in range(len(A)):
            pre[i + 1] = pre[i] + A[i]

        if pre[-1] % 3 != 0:
            return False

        target = pre[-1] // 3
        i = 1
        while i < len(pre):
            if pre[i] != target:
                i += 1
            else:
                break

        if i == len(pre):
            return False

        for j in range(i + 1, len(pre)):
            if pre[j] - pre[i] == target:
                return True

        return Flase


if __name__ == '__main__':
    print(Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
