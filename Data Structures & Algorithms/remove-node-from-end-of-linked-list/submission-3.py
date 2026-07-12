# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        dummy_head = ListNode()
        dummy_head.next = head

        tail = head
        while tail.next:
            tail = tail.next
            size += 1

        if size - n == 0:
            return head.next

        dummy = head
        for i in range(size - n):
            dummy_head = dummy
            dummy = dummy.next

        dummy_head.next = dummy.next

        return head
