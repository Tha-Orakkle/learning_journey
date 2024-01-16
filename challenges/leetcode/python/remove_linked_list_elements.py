#!/usr/bin/python3
"""removes from a linked lst a node with a value
that matches the value passed"""

class ListNode:
    """represents the node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        """removes the node that matches"""
        if not head:
            return None
        temp = head
        while temp and temp.next:
            next_node = temp.next
            if next_node.val == val:
                temp.next = next_node.next
                continue
            temp = temp.next
        if head.val == val:
            head = head.next
        return head
