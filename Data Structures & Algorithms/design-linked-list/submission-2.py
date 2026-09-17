class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        tmp = self.head.next
        for i in range(index):
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, next = self.head.next, prev = self.head)
        node.next.prev = node
        node.prev.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val, next = self.tail, prev = self.tail.prev)
        node.next.prev = node
        node.prev.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif not index:
            self.addAtHead(val)
        elif index < self.size:
            tmp = self.head.next
            for i in range(index):
                tmp = tmp.next
            node = ListNode(val, next = tmp, prev = tmp.prev)
            node.next.prev = node
            node.prev.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            tmp = self.head.next
            for i in range(index):
                tmp = tmp.next
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)