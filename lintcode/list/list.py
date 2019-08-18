# -*-coding:utf-8-*-

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        if head == None: return
        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead
        while head:
            if head.val < x:
                aTail.next = head
                aTail = aTail.next
            else:
                bTail.next = head
                bTail = bTail.next
            head = head.next
        bTail.next = None
        aTail.next = bHead.next
        return aHead

    def removeNode(self,head,target):
        curr=head
        if head==target:
            curr=head.next
            head.next=None
            return curr

        while curr:
            if curr.next ==target:
                a=curr.next
                curr.next=a.next
                a.next=None
            curr=curr.next
        return head




node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
solution = Solution()
solution.removeNode(node1,node1)
solution.partition(node1, 4)
