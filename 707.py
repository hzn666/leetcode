class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.count = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.count:
            node = self.head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self.count:
            return

        self.count += 1

        add_node = ListNode(val)
        prev_node, cur_node = None, self.head
        for _ in range(index + 1):
            prev_node, cur_node = cur_node, cur_node.next
        else:
            prev_node.next, add_node.next = add_node, cur_node

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.count:
            self.count -= 1

            prev_node, cur_node = None, self.head

            for _ in range(index + 1):
                prev_node, cur_node = cur_node, cur_node.next
            else:
                prev_node.next, cur_node.next = cur_node.next, None


# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
# linkedList.get(1);            //返回2
# linkedList.deleteAtIndex(1);  //现在链表是1-> 3
# linkedList.get(1);            //返回3

linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)

node = linkedList.head.next
for _ in range(linkedList.count):
    print(node.val)
    node = node.next
