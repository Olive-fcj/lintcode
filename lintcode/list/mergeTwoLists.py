#-*-coding:utf-8-*-
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None: return None
        if l1 is None: return l2
        if l2 is None: return l1
        curr1=l1
        curr2=l2
        head=ListNode(0)
        curr3=head
        while curr1 and curr2:
            if curr1.val >= curr2.val:
                curr3.next =curr2
                curr3 = curr3.next
                curr2=curr2.next
            else:
                curr3.next=curr1
                curr3 = curr3.next
                curr1=curr1.next
        if curr1 is not None:curr3.next=curr1
        if curr2 is not None:curr3.next=curr2
        print(curr3)
        return curr3.next


l1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(6)
l1.next = node2
node2.next = node3
node3.next = node4

l2 = ListNode(1)
node5 = ListNode(3)
l2.next = node5

solution = Solution()
solution.mergeTwoLists(l1,l2)

