# def is_valid(ls1, ls2):
#     if len(ls1) != len(ls2):
#         return False

#     def find(ls1, ls2):
#         if not ls1:
#             return True

#         num = ls2[0]
#         if num not in ls1:
#             return False
#         location_in_ls1 = ls1.index(num)

#         part_in_ls1 = ls1[0: location_in_ls1 + 1]
#         part_in_ls1.reverse()

#         if part_in_ls1 != ls2[0: location_in_ls1 + 1]:
#             return False
#         else:
#             return find(ls1[location_in_ls1 + 1:], ls2[location_in_ls1 + 1:])

#     return find(ls1, ls2)

def is_valid(ls1, ls2):
    stack = []
    index = 0

    for i in range(len(ls1)):
        stack.append(ls1[i])

        while stack and stack[-1] == ls2[index]:
            stack.pop()
            index += 1

    return len(stack) == 0


if __name__ == '__main__':
    # key point: 不重复元素
    # 找到2中的第一个值，找到在1中的对应位置，判断是否逆序
    # 递归直至为空
    ls1 = [0, 1, 2, 3, 4]
    ls2 = [2, 1, 0, 4, 3]
    print(is_valid(ls1, ls2))
    ls1 = [0]
    ls2 = [0]
    print(is_valid(ls1, ls2))
    ls1 = [0]
    ls2 = [2]
    print(is_valid(ls1, ls2))
