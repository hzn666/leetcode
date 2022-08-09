class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


input_list = list(map(int, input().split()))
n = input_list[0]
num = [input_list[1]]
num_list = input_list[2:2 * n]
delete_num = input_list[-1]

for i in range(0, len(num_list), 2):
    index = num.index(num_list[i + 1])
    num.insert(index + 1, num_list[i])

dummy = ListNode(-1)
cur = dummy

for i in num:
    node = ListNode(i)
    cur.next = node
    cur = node

cur = dummy.next
while cur:
    if cur.val != delete_num:
        print(cur.val, end=" ")
    cur = cur.next
