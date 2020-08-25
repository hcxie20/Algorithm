class Solution:
    def coinChange(self, nums, amount):
        self.rst = float("inf")
        coins = [13, 11, 7, 3, 1]
        l = len(coins)
        nums.sort(reverse=True)

        def greddy(remains, coinID, count):
            if remains == 0:
                    self.rst = min(self.rst, count)

            if coinID >= l:
                return

            if remains != 0:
                num = min(remains//nums[coinID], nums[coinID])
                for i in range(num, -1, -1):
                    if i + count < self.rst:
                        greddy(remains - coins[coinID] * i, coinID + 1, count + i)
                    else: return

        greddy(amount, 0, 0)

        if self.rst == float("inf"):
            return -1
        return self.rst

print(Solution().coinChange([1, 2, 3, 4, 5], 30))