#!/usr/bin/python3
"""Merges a sorted array of integers with in-place modification"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while(True):
            if len(nums1) == m:
                break
            nums1.pop()
        nums1 += nums2
        nums1.sort()
