class Solution:
    def canArrange(self, arr, k):
        seen_dict = {}

        for dig in arr:
            tmp = dig % k

            if tmp not in seen_dict:
                seen_dict[tmp] = 1
            else:
                seen_dict[tmp] += 1

        if 0 in seen_dict and seen_dict[0] % 2 != 0:
            return False

        for i in range(1, k):
            if i not in seen_dict:
                continue

            if k - i not in seen_dict or seen_dict[i] != seen_dict[k - i]:
                return False

        return True


if __name__ == '__main__':
    print(Solution().canArrange([-10, 10], 2))
    print(Solution().canArrange([-1,1,-2,2,-3,3,-4,4], 3))
