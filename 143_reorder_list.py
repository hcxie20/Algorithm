# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid node
        dumbHead = ListNode(None)
        dumbHead.next = head
        p1 = p2 = dumbHead

        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next

        mid = p1.next
        p1.next = None

        # reverse mid ->
        p1 = None
        p2 = mid

        while p2 != None:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp

        # merge to list
        # p2(right list) is equal to head, or less than 1
        p2 = p1
        p1 = head
        while p2 != None:
            tmp = p1.next
            p1.next = p2
            p2 = p2.next
            p1.next.next = tmp
            p1 = tmp
        return head

ls = ListNode("1")
ls.next = ListNode("2")
ls.next.next = ListNode("3")
ls.next.next.next = ListNode("4")
ls.next.next.next.next = ListNode("5")

print(Solution().reorderList(ls))













        
