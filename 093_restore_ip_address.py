class Solution:
    def restoreIpAddresses(self, s):
        def restoreIpAddresses(self, s):
        rst = []
        n = len(s)
        if n > 12:
            return rst
    
        def setDot(prev, remain, addr):
            i = prev + 1
            while i < n + 1 and i < prev + 4:
                segment = s[prev:i]
                if valid(segment):
                    if len(addr) == 0:
                        new_addr = addr + segment
                    else:
                        new_addr = addr + "." + segment
                    if remain == 1 and i == n:
                        rst.append(new_addr)
                    else:
                        setDot(i, remain-1, new_addr)
                i += 1

        def valid(s):
            if s[0] != "0":
                return int(s) <= 255
            else:
                return len(s) == 1

        setDot(0, 4, "")
        return rst

print(Solution().restoreIpAddresses("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"))