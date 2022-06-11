class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(next=head)

    fast, slow = dummy, dummy

    while n >= 0:
        fast = fast.next
        n -= 1

    while not fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
