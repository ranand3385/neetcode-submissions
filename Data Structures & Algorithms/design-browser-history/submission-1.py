class ListNode:
    def __init__(self, url = "", next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        dummy = ListNode(url)
        self.cur.next = dummy
        dummy.prev = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps:
            steps -= 1
            self.cur = self.cur.prev
        return self.cur.url

    def forward(self, steps: int) -> str:
        while self.cur.next and steps:
            steps -= 1
            self.cur = self.cur.next
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)