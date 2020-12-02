import re
'''
# A
## B
### C
'''

class Solotion(object):
    def __init__(self):
        pass

    def gerenate_tiles(self, strings):
        seen_dict = {}
        last_seen_level = 0
        level_depth = 0

        for string in strings:
            title_level = self.parse_title(string)

            if title_level > last_seen_level:
                level_depth += 1

            elif title_level < last_seen_level:
                for i in range(title_level + 1, level_depth + 1):
                    seen_dict[i] = 0

                level_depth -= 1

            last_seen_level = title_level

            if title_level not in seen_dict:
                seen_dict[title_level] = 1

            else:
                seen_dict[title_level] += 1

            tmp = []
            for i in range(1, level_depth + 1):
                tmp.append(str(seen_dict[i]))

            title = '.'.join(tmp)

            string = title + string[title_level:]

        return strings

    @staticmethod
    def parse_title(string):
        pattern = re.compile(r'#+ ')
        rst = re.search(pattern, string)

        if rst:
            return len(rst[0]) - 1

        else:
            return None


if __name__ == '__main__':
    strings = [
        '# A',
        '## B',
        '### C',
        '# A',
        '## B',
        '### C',
        '### what does # do'
    ]

    solution = Solotion()
    print(solution.gerenate_tiles(strings))
