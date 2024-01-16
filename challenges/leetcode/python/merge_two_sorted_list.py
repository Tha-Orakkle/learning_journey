#!/usr/bin/python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def append_node(node, value):
    new_node = ListNode(val=value)
    if not node:
        node = new_node
        return
    current = node
    while current.next:
        current = current.next
    current.next = new_node

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list1 and not list2:
            return None
        current1, current2 = list1, list2
        if list1.val <= list2.val:
            merged_list = ListNode(list1.val)
            current1 = list1.next
        else:
            merged_list = ListNode(list2.val)
            current2 = current2.next

        while current1 and current2:
            if current1.val <= current2.val:
                append_node(merged_list, current1.val)
                current1 = current1.next
            else:
                append_node(merged_list, current2.val)
                current2 = current2.next
        while current1:
            append_node(merged_list, current1.val)
            current1 = current1.next
        while current2:
            append_node(merged_list, current2.val)
            current2 = current2.next

        return merged_list
