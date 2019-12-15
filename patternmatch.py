class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # https://www.youtube.com/watch?v=l3hda49XcDE&list=PLrmLmBdmIlpuE5GEMDXWf0PWbBD9Ga1lO
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        # dp [0][], dp[][0] all false !! if the start of the pattern is not a *
        for i in range(1, len(p)+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == ".":
                    # same character, including "."
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    # "*"
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == "." or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    # not same character
                    dp[i][j] = False
        return dp[len(s)][len(p)]

if __name__ == '__main__':
    a = Solution()
    print(a.isMatch("aab", "c*a*b"))
    