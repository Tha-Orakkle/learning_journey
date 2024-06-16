#!/usr/bin/python3
"""Finds the median of two sorted arrays"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array = nums1 + nums2
        merged_array.sort()
        _len = len(merged_array)
        if _len % 2 == 0:
            m = merged_array[_len // 2] + merged_array[(_len // 2) - 1]
            m  = m / 2
        else:
            m = merged_array[_len // 2]
        return m

if __name__ == "__main__":
    a = Solution()
    print(a.findMedianSortedArrays([1, 3], [2]))
