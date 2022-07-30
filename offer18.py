class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head, val):
        root = ListNode(0)
        root.next = head

        pre = root
        cur = head

        while cur:
            if cur.val == val:
                pre.next = cur.next
                return root.next
            else:
                pre = cur
                cur = cur.next

    def deleteNode1(self, head, val):
        if head.val == val:
            return head.next

        pre, cur = head, head.next

        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head
