from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reversePrint(head: ListNode) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res[::-1]
