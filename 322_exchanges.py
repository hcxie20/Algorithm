class Solution:
    def coinChange(self, coins, amount):
        self.rst = float("inf")
        l = len(coins)
        coins.sort(reverse=True)
        
        def greddy(remains, coinID, count):
            if remains == 0:
                    self.rst = min(self.rst, count)

            if coinID >= l:
                return
                
            if remains != 0:
                for i in range(remains//coins[coinID], -1, -1):
                    if i + count < self.rst:
                        greddy(remains - coins[coinID] * i, coinID + 1, count + i)
                    else: return

        greddy(amount, 0, 0)

        if self.rst == float("inf"):
            return -1
        return self.rst

print(Solution().coinChange([1,2,5], 11))