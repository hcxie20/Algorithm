# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        def mergeSort(ls):
            l, r = self.findMid(ls)
            if l is r:
                # same, len(ls) == 1
                return ls

            l = mergeSort(l)
            r = mergeSort(r)

            p1 = l
            p2 = r

            rst = ListNode(None)
            tmp = rst
            while p1 and p2:
                if p1.val < p2.val:
                    tmp.next = p1
                    p1 = p1.next
                else:
                    tmp.next = p2
                    p2 = p2.next
                tmp = tmp.next
            if p1:
                tmp.next = p1
            if p2:
                tmp.next = p2
            return rst.next

        head = mergeSort(head)
        return head
    
    @staticmethod
    def findMid(ls):
        # cut ls in middle
        # length of p1 always <= p2
        # return lsLeft, lsRight
        # if len(ls) == 1:
        # return would be ls, ls
        dumbHead = ListNode(None)
        dumbHead.next = ls

        p1 = p2 = dumbHead

        while p2.next != None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next

        p2 = p1.next
        p1.next = None
        return ls, p2
            