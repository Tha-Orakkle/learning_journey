#!/usr/bin/python3
"""Returns the majority element"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checked = set()
        maj = 0
        for num in nums:
            if num not in checked:
                checked.add(num)
                count = 0
                for n in nums:
                    if n == num:
                        count += 1
                if count > maj:
                    maj = count
                    maj_value = num
        return maj_value
