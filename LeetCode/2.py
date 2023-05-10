# 2. Add Two Numbers - Medium

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#  iterate through the two linked lists simultaneously and add the corresponding digit values from each list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        aux_list = ListNode()
        current = aux_list
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total_sum = val1 + val2 + carry

            carry = total_sum // 10
            current_val = total_sum % 10

            new_node = ListNode(current_val)
            current.next = new_node
            current = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return aux_list.next
