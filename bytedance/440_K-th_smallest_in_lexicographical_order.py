class Solution:
    def findKthNumber(self, n, k):
        # (pointer -> i), i in list
        i = 1
        pointer = 1
        while pointer != k:
            count = self.count(i, n)
            if pointer + count > k:
                i *= 10
                pointer += 1
            elif pointer + count <= k:
                i += 1
                pointer += count
        return i

    def count(self,i, n):
        count = 0
        a = i
        b = i + 1
        while a <= n:
            count += min(n+1, b) - a
            a *= 10
            b *= 10
        return count

print(Solution().findKthNumber(22, 12))