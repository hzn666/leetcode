# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        first = head
        last = head

        for i in range(k):
            first = first.next

        while first:
            first = first.next
            last = last.next

        return last
