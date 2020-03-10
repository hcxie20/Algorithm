class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        p1, p2 = l1, l2
        rst = ListNode(None)
        tmp = rst
        while p1 != None or p2 != None:
            if p1 == None:
                tmp.next = p2
                return rst.next
            elif p2 == None:
                tmp.next = p1
                return rst.next
            else:
                if p1.val <= p2.val:
                    tmp.next = p1
                    p1 = p1.next
                else:
                    tmp.next = p2
                    p2 = p2.next
                tmp = tmp.next