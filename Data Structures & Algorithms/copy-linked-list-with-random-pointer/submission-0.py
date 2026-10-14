"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNode = collections.defaultdict(lambda: Node(0))
        oldNode[None] = None

        cur = head

        while cur:
            oldNode[cur].val = cur.val
            oldNode[cur].next = oldNode[cur.next]
            oldNode[cur].random = oldNode[cur.random]
            cur = cur.next

        return oldNode[head]


        