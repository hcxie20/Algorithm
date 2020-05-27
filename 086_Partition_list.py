# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        
        dumb_small = ListNode(None)
        dumb_big = ListNode(None)

        small = dumb_small
        big = dumb_big

        cur = head
        while cur != None:
            next = cur.next
            cur.next = None

            if cur.val < x:
                dumb_small.next = cur
                dumb_small = dumb_small.next
            else:
                dumb_big.next = cur
                dumb_big = dumb_big.next
            
            cur = next
        
        dumb_small.next = big.next

        return small.next