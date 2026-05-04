# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2

        new = ListNode()
        cur_new = new
        
        while list1 and list2:
            if list1.val<list2.val:
                cur_new.next = list1
                list1 = list1.next
            else:
                cur_new.next = list2
                list2 = list2.next
            cur_new = cur_new.next
        if list1:
            cur_new.next = list1
        else:
            cur_new.next = list2
        
        return new.next




