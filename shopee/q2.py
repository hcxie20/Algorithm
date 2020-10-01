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
