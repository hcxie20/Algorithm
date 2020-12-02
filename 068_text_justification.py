class Solution:
    def fullJustify(self, words, maxWidth: int):
        rst = []
        to_do_ls = []

        remains = maxWidth + 1
        total_length = 0
        i = 0
        for i in range(len(words)):
            if remains < len(words[i]) + 1:
                rst.append(self.parse_line(to_do_ls, maxWidth, total_length, False))
                to_do_ls = []
                total_length = 0
                remains = maxWidth + 1

            total_length += len(words[i])
            to_do_ls.append(words[i])
            remains -= len(words[i]) + 1

        if to_do_ls:
            rst.append(self.parse_line(to_do_ls, maxWidth, total_length, True))

        return rst

    @staticmethod
    def parse_line(words, maxWidth, total_length, last_line):
        if last_line:
            s = ' '.join(words)
            s += (maxWidth - len(s)) * ' '
            return s

        if len(words) == 1:
            return words[0] + ' ' * (maxWidth - len(words[0]))

        extra_spaces = maxWidth - total_length
        extra_spaces_each = extra_spaces // (len(words) - 1)
        extra_spaces_extra = extra_spaces % (len(words) - 1)

        rst = ''
        for i in range(len(words) - 1):
            rst += words[i]
            rst += ' ' * extra_spaces_each

            if extra_spaces_extra:
                rst += ' '
                extra_spaces_extra -= 1

        rst += words[-1]

        return rst


if __name__ == '__main__':
    ls = ["This", "is", "an", "example", "of", "text", "justification."]
    # ls = ["What","must","be","acknowledgment","shall","be"]
    length = 16

    print(Solution().fullJustify(ls, length))
