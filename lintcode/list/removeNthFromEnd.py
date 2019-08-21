# -*-coding:utf-8-*-

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    if head.next == None: return None
    curr = head
    a = 0
    while curr:
        a += 1
        curr = curr.next
        if a == n:
            target = head
        if a > n:
            target = target.next
        if curr.next == None:
            if target:
                b = target.next
                target.next = b.next
                b.next = None
                return head
            else:
                return head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

removeNthFromEnd(node1, 5)


