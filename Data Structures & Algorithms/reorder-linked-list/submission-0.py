# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return None

        queue = deque()
        current = head
        while current:
            queue.append(current)
            current = current.next
        
        current = queue.popleft()
        while queue:
            if queue:
                first = queue.pop()
                current.next = first
                current = first
            if queue:
                second = queue.popleft()
                current.next = second
                current = second
        
        current.next = None

        
