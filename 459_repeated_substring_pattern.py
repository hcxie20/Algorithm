class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def kmp(s):
            ls = [0] * len(s)
            j = 0
            i = 1
            while i < len(s):
                if s[i] == s[j]:
                    ls[i] = j + 1
                    j += 1
                    i += 1
                else:
                    if j > 0:
                        j = ls[j - 1]
                    else:
                        ls[i] = 0
                        i += 1
            return ls
        
        ls = kmp(s)
        if ls[-1] == 0:
            return False
        else:
            return len(ls) % (len(ls) - ls[-1])==0



'''
KMP
'''