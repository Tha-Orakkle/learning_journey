#!/usr/bin/python3
"""Removes element from an array of integers where element
equals a given integer"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums.pop(idx)
            else:
                idx += 1
        return len(nums)
