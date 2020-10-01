# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return []

        listscopy = lists[:]
        while len(listscopy) != 1:
            i = 0
            while len(listscopy) - i > 1:
                listscopy[i] = self.merge2Lists(listscopy[i], listscopy[i+1])
                listscopy.pop(i+1)
                i += 1

        return listscopy[0]

    @staticmethod
    def merge2Lists(list1, list2):
        dumbHead = ListNode(None)
        tmp = dumbHead

        p1 = list1
        p2 = list2

        while p1 != None or p2 != None:
            if p1 == None:
                tmp.next = p2
                break
            elif p2 == None:
                tmp.next = p1
                break
            else:
                if p1.val <= p2.val:
                    tmp.next = p1
                    p1 = p1.next
                else:
                    tmp.next = p2
                    p2 = p2.next
                tmp = tmp.next
        return dumbHead.next


ls1 = ListNode(1)
ls1.next = ListNode(4)
ls1.next.next = ListNode(5)

ls2 = ListNode(1)
ls2.next = ListNode(3)
ls2.next.next = ListNode(4)

ls3 = ListNode(2)
ls3.next = ListNode(6)

ls = [ls1, ls2, ls3]

print(Solution().mergeKLists(ls))