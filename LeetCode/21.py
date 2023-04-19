# 21. Merge Two Sorted Lists - Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # handle empty lists
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # initialize pointers for both lists and a new dummy head node
        pointer1, pointer2 = list1, list2
        new_head = ListNode(-1)
        current = new_head
        
        # merge the lists
        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next
            current = current.next
        
        # append any remaining nodes from the non-empty list
        if pointer1:
            current.next = pointer1
        elif pointer2:
            current.next = pointer2
        
        return new_head.next