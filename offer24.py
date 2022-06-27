class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    def recur(cur, pre):
        if not cur:
            return pre
        res = recur(cur.next, cur)
        cur.next = pre
        return res

    return recur(head, None)
