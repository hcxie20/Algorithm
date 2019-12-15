class Substring(object):
    def __init__(self, str1, str2):
        
        def find_string(str1, str2):
            dp = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
            for i in range(1, len(str2) + 1):
                for j in range(1, len(str1) + 1):
                    if str1[j - 1] == str2[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
            max_value = max(max(row) for row in dp)
            row = [max(row) for row in dp].index(max_value)
            # column = dp[row].index(max_value)
            rst = str2[row - max_value:row]
            pass

        
        find_string(str1, str2)




if __name__ == "__main__":
    a = "abcacbcbd"
    b = "ccb"
    c = Substring(a, b)
