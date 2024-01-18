#!/usr/bin/python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = flag = 0
        result = ListNode()
        current = result
        while (l1 or l2 or carry):
            if flag == 1:
                current.next = ListNode()
                current = current.next
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            _sum = x + y + carry

            carry = _sum // 10
            current.val = _sum % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            flag = 1
        return result
