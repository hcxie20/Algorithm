class Solution:
    def myAtoi(self, str: str) -> int:
        neg = 0
        for i in range(len(str)):
            if str[i] == " ":
                pass
            elif str[i] == "-" or "0" <= str[i] <= "9":
                # numbers starts here
                if str[i] == "-":
                    rst = int(str[i+1])
                    neg = 1
                    i += 2
                else:
                    rst = int(str[i])
                    i += 1
                    
                while i < len(str) and "0" <= str[i] <= "9":
                    rst *= 10
                    rst += int(str[i])
                    i += 1
                if neg: 
                    if rst > 2147483648:
                        return -2147483648
                    else:
                        return -rst
                else: 
                    if rst > 2147483647:
                        return 2147483647
                    else:
                        return rst
            else:
                return 0

print(Solution().myAtoi("423"))