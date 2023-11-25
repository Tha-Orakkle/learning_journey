#!/usr/bin/python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        temp = head
        while temp and temp.next:
            next_node = temp.next
            if next_node.val == temp.val:
                temp.next = next_node.next
                continue
            temp = temp.next
        return head
