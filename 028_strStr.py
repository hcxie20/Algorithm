class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        tmp = 0
        l = len(needle)
        if len(haystack) == 0 and l == 0:
            return 0
        while tmp + l <= len(haystack):
            if haystack[tmp:tmp+l] == needle:
                return tmp
            tmp += 1
        return -1