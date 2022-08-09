class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


while True:
    try:
        n = int(input())
        num = list(map(int, input().split()))
        delete = int(input())

        dummy = ListNode(-1)
        cur = dummy

        for i in num:
            node = ListNode(i)
            cur.next = node
            cur = node

        first = dummy.next
        for i in range(delete):
            first = first.next

        last = dummy.next
        while first:
            first = first.next
            last = last.next
        print(last.val)
    except:
        break
