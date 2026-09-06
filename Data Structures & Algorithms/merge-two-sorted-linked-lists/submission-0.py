# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0, None)

        while list1 and list2:
            v1 = list1.val
            v2 = list2.val 

            if v1 < v2:
                cur.next = ListNode(v1)
                list1 = list1.next
            else:
                cur.next = ListNode(v2)
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2

        return dummy.next


