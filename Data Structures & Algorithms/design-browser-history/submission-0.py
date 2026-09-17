class ListNode:
    def __init__(self, url = "", next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode("")
        self.tail = ListNode("")
        home = ListNode(homepage, prev = self.head, next = self.tail)
        self.head.next = home
        self.tail.prev = home
        self.curr = home

    def visit(self, url: str) -> None:
        dummy = ListNode(url)
        dummy.prev = self.curr
        dummy.next = self.tail
        self.tail.prev = dummy
        self.curr.next = dummy
        self.curr = dummy
        

    def back(self, steps: int) -> str:
        while self.curr.prev.prev and steps:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url


    def forward(self, steps: int) -> str:
        while self.curr.next.next and steps:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)