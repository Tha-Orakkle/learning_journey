#!/usr/bin/python3
"""
Finds the index of a number in a list.
If number not in list, finds the index number would have been"
"""


class Solution:
    def searchInsert(self, nums, target):
        try:
            idx = nums.index(target)
        except ValueError:
            l = len(nums)
            if target > nums[l - 1]:
                idx = l
            elif target < nums[l - 1]:
                for i in range(0, l):
                    if nums[i] > target:
                        idx = i
                        break
        return idx

if __name__ == "__main__":
    a = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    print(a.searchInsert(nums, target))
