# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        checkLen = head
        length = 0
        while checkLen:
            checkLen = checkLen.next
            length += 1
        
        nodeN = length - n
        if nodeN == 0:
            return head.next 
        
        temp = head
        
        for i in range(nodeN-1):
            temp = temp.next
            print(temp.val)
        
        temp.next = temp.next.next
    
        return head

        
        
        
            
        


