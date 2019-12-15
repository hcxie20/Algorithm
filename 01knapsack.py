class Solution(object):
    def __init__(self, wt, val, total):
        dp = [[0 for i in range(total + 1)] for j in range(len(wt))]
        for i in range(1, total + 1):
            dp[0][i] = val[0]

        for i in range(1, len(wt)):
            for j in range(1, total + 1):
                if wt[i] <= j:
                    dp[i][j] = max(dp[i - 1][j], val[i] + dp[i-1][j-wt[i]])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        self.max = dp[i][j]
        self.list = []
        while i != 0:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                j -= wt[i]
                self.list.insert(0, i)
                i -= 1
                
        pass




if __name__ == "__main__":
    wight = [1, 3, 4, 5]
    value = [1, 4, 5, 7]
    total = 7
    a = Solution(wight, value, total)
