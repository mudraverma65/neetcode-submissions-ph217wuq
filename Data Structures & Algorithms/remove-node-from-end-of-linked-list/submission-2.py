# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or n <=0:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        start, last = dummy, dummy

        for _ in range(0, n):
            if not last.next:
                return None
            last = last.next

        while last.next:
            last = last.next
            start = start.next
        
        start.next = start.next.next
        return dummy.next