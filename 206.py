class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    tmp = None
    pre = None
    cur = head

    while cur != None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return pre
