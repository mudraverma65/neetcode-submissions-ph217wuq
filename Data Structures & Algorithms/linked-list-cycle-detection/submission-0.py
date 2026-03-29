# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Assuming no duplicates

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head

        while current:
            if current in visited:
                return True
                break
            else:
                visited.add(current)
                current= current.next
            
        return False


        