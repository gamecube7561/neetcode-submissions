# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy1 = list1
        dummy2 = list2
        dummy3 = dummy

        while dummy1 or dummy2:
            if dummy1 and dummy2:
                if dummy1.val <= dummy2.val:
                    dummy.next = dummy1
                    dummy1 = dummy1.next
                else:
                    dummy.next = dummy2
                    dummy2 = dummy2.next
            elif dummy1 and not dummy2:
                dummy.next = dummy1
                dummy1 = dummy1.next
            elif dummy2 and not dummy1:
                dummy.next = dummy2
                dummy2 = dummy2.next
            dummy = dummy.next
        
        return dummy3.next
        

        