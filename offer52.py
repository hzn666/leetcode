class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        cur_a = headA
        cur_b = headB

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB
            cur_b = cur_b.next if cur_b else headA

        return cur_a