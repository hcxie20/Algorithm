# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rst = ListNode(None)
        tmp = rst
        
        carry = 0
        p1 = l1
        p2 = l2

        while p1 != None or p2 != None or carry:
            if p1 == None and p2 == None:
                tmp.next = ListNode(1)
                break
            elif p1 == None:
                carry, val = divmod(p2.val + carry, 10)
                p2 = p2.next
            elif p2 == None:
                carry, val = divmod(p1.val + carry, 10)
                p1 = p1.next
            else:
                carry, val = divmod(p1.val + p2.val + carry, 10)
                p1 = p1.next
                p2 = p2.next
            tmp.next = ListNode(val)
            tmp = tmp.next

        return rst.next