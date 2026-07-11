# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        prev = head
        dummy = head
 
        while dummy and dummy.next:
            while dummy.next.next:
                dummy = dummy.next
            tail = dummy.next
            dummy.next = None
            tail.next = prev.next
            prev.next = tail
            
            prev = prev.next.next
            dummy = prev.next

        return None