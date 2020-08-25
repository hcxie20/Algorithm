import collections

def find_substring(src, target):
    if not src or not target:
        return []

    p = 0

    letter_dict = collections.defaultdict(int)
    occurance_ls = []

    rst = []

    while p < len(src):
        current_letter = src[p]
        if current_letter not in target:
            p += 1
            continue

        else:
            occurance_ls.append(p)
            letter_dict[current_letter] += 1
            if len(letter_dict) == len(target):
                while True:
                    if letter_dict[src[occurance_ls[0]]] > 1:
                        letter = occurance_ls.pop(0)
                        letter_dict[letter] -= 1
                    else:
                        rst = src[occurance_ls[0]: p + 1]
                        break

            p += 1

    return rst


if __name__ == '__main__':
    '''
    思路：滑动窗口？？
    移动p使得第一次找齐所有字母，途中使用字典记录每个字母的数量， occurance_ls记录所有出现字母的位置
    之后（包括第一次找齐）每次找齐，尝试缩短窗口：
        检查occur_ls的第一个值，查看对应的字母以及字母在字典里的数量
            若大于1，即可缩小，此时对应字典值减一
        重复至不能缩小（第一个值只出现一次）
    移动p到结束即是答案
    '''
    src = 'ASKSBACWDMVJDNAHFNFJ'
    target = 'ABCD'
    print(find_substring(src, target))
    src = 'ABCD'
    target = 'ABCD'
    print(find_substring(src, target))
