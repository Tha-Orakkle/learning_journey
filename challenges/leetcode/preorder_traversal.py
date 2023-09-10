#!/usr/bin/python3
"""preorder traversal of a binary tree"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        result = [root.val]
        left = self.preorderTraversal(root.left)
        result = result + left
        right = self.preorderTraversal(root.right)
        result = result + right

        return result
