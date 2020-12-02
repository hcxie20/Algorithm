# find k list,
# a -> b -> head -> ... -> tail -> c
# 2 pointers point to b and c
# b: prev
# head: head
# tail: tail
# c: tail.next
# slice it (tail.next = None)
# call reverse head to tail, return new head(actually tail)
# a -> b    <- head <- ... <- tail     c
# b.next = tail
# head.next = c
#
# prev = tail
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dumbhead = ListNode(None)
        dumbhead.next = head

        tmpNode = ListNode(None)
        prev = dumbhead
        while prev.next != None:
            start = prev.next
            end = start
            for _ in range(k-1):
                if end.next == None:
                    return dumbhead.next

                end = end.next

            # now a -> b(prev) -> start -> ... -> end -> c(tmp)
            tmp = end.next
            end.next = None
            # reverse list
            p0 = tmpNode
            p1 = start
            while p1 != None:
                p2 = p1.next
                p1.next = p0
                p0 = p1
                p1 = p2

            # a -> b(prev)    tmpNode <- start <- ... <- end     c(tmp)
            start.next = tmp
            prev.next = end
            # a ->b(prev) -> end -> ... -> start -> c(tmp)
            prev = start

        return dumbhead.next