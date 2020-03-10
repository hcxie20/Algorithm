# p1, p2 = head1, head2
# p1, p2 后移。当p1到尾，转到head2
# 若p1, p2相遇，则这个点重复
# 若两个链表尾不相等，则一定无交叉



#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB

        endVal = None
        while True:
            if p1.val == p2.val:
                return p1.val
            if p1.next != None:
                p1 = p1.next
            else:
                if endVal is None:
                    endVal = p1.val
                else:
                    if endVal != p1.val:
                        return False                      
                p1 = headB

            if p2.next != None:
                p2 = p2.next
            else:
                if endVal is None:
                    endVal = p2.val
                else:
                    if endVal != p2.val:
                        return False
                p2 = headA
        return

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)

head2 = ListNode(2)
head2.next = ListNode(3)
print(Solution().getIntersectionNode(head1, head2))