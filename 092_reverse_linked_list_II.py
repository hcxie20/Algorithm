# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m: int, n: int):
        dumbHead = ListNode(None)
        dumbHead.next = head
        p1 = head
        prev = dumbHead
        for _ in range(m-1):
            prev = p1
            p1 = p1.next

        prev.next = None
        tail = p1

        p2 = None
        for _ in range(n-m+1):
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp

        prev.next = p2
        tail.next = p1
        return dumbHead.next

ls = ListNode(1)
ls.next = ListNode(2)

Solution().reverseBetween(ls, 1, 2)