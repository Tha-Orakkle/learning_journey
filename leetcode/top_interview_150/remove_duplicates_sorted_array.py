#!/usr/bin/python3
"""Removes duplicates from sorted Array.
Modification done in-place"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = set()
        idx = 0

        while idx < len(nums):
            if nums[idx] in uniq:
                nums.pop(idx)
            else:
                uniq.add(nums[idx])
                idx += 1
        return len(nums)
