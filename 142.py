class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            index1 = head
            index2 = slow

            while index1 != index2:
                index1 = index1.next
                index2 = index2.next

            return index1

    return None
