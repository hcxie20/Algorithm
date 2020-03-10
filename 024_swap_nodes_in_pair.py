# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        dumbhead = ListNode(None)
        dumbhead.next = head
        
        # p0 prev node of p1
        p0 = dumbhead
        # p1 front pointer
        p1 = dumbhead
        p2 = dumbhead

        # after reverse, p2 actually is the front pointer
        # p2 -> p1 -> x -> y ->
        while p1.next != None and p1.next.next != None:
            # at start, p1 still need to be the front pointer
            # p2 -> p1(p0) -> new p1 -> new p2 -> z(tmp) -> ...
            p0 = p1
            p1 = p1.next
            p2 = p1.next

            tmp = p2.next
            p2.next = p1
            p0.next = p2
            p1.next = tmp

        return dumbhead.next