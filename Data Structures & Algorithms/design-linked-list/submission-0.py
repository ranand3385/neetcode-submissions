class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        tmp = self.head.next
        while tmp and index != 0:
            tmp = tmp.next
            index -= 1
        if not index and tmp and tmp.next:
            return tmp.val

        return -1
        

    def addAtHead(self, val: int) -> None:
        dummy = ListNode(val)
        dummy.next = self.head.next
        dummy.prev = self.head
        self.head.next.prev = dummy
        self.head.next = dummy
        


    def addAtTail(self, val: int) -> None:
        dummy = ListNode(val)
        dummy.next = self.tail
        dummy.prev = self.tail.prev
        self.tail.prev.next = dummy
        self.tail.prev = dummy


    def addAtIndex(self, index: int, val: int) -> None:
        dummy = ListNode(val)
        tmp = self.head.next
        while tmp and index != 0:
            index -= 1
            tmp = tmp.next
        if not index and tmp:
            dummy.next = tmp
            dummy.prev = tmp.prev
            tmp.prev.next = dummy
            tmp.prev = dummy
            


    def deleteAtIndex(self, index: int) -> None:
        tmp = self.head.next
        while tmp and index != 0:
            index -= 1
            tmp = tmp.next
        if not index and tmp and tmp.next:
            tmp.next.prev = tmp.prev
            tmp.prev.next = tmp.next
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)