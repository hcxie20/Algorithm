class Solution:
    def getMinLen(self , str ):
        if len(str) == 1:
            return 0

        # write code here
        def valid_pattern(target, pattern):
            l = len(pattern)
            i = 0
            while i < len(target):
                if i + l <= len(target) - 1:
                    compare_in_target = target[i:i + l]
                    # end = i + l
                else:
                    compare_in_target = target[i:]
                    # end = len(target)

                if pattern == compare_in_target:
                    i = i + l
                else:
                    left_over = len(compare_in_target)
                    if left_over >= l:
                        return False, None

                    if pattern[:left_over] == compare_in_target:
                        return True, l - left_over
                    else:
                        return False, None

            return True, 0


        for i in range(1, len(str) + 1):
            pattern = str[:i]
            valid, lack = valid_pattern(str, pattern)
            if valid:
                return lack


if __name__ == '__main__':
    # print(Solution().getMinLen('abcabca'))
    # print(Solution().getMinLen('a'))
    print(Solution().getMinLen('ab'))
class Solution(object):
    def equal_string(self, s1, s2):
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        if len(s1) % 2 != 0 or len(s2) % 2 != 0:
            return False

        dct = {}

        for l in s1:
            if l in dct:
                dct[l] += 1
            else:
                dct[l] = 1

        for l in s2:
            if l not in dct:
                return False

            else:
                dct[l] -= 1
                if dct[l] < 0:
                    return False

        s1p1 = s1[:int(len(s1) / 2)]
        s1p2 = s1[int(len(s1) / 2):]
        s2p1 = s2[:int(len(s2) / 2)]
        s2p2 = s2[int(len(s2) / 2):]

        return self.equal_string(s1p1, s2p1) or self.equal_string(s1p2, s2p1) or self.equal_string(s1p1, s2p2) or self.equal_string(s1p2, s2p2)


if __name__ == '__main__':
    print(Solution().equal_string('aaba', 'abaa'))
    print(Solution().equal_string('aaba', 'aaaa'))
    print(Solution().equal_string('aaba', ''))
    print(Solution().equal_string('', ''))
    print(Solution().equal_string('aaaba', 'aaaab'))
