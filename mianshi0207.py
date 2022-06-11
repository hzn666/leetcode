class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    cur_a = headA
    cur_b = headB

    while cur_a != cur_b:
        cur_a = cur_a.next if cur_a else headB
        cur_b = cur_b.next if cur_b else headA

    return cur_a
