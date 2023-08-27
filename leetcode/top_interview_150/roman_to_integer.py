#!/usr/bin/python3
"""converts Roman Numerals to Integer"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicto = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = dicto.get(s[0])

        for i in range(1, len(s)):
            prev = dicto.get(s[i - 1])
            current = dicto.get(s[i])
            if prev < current:
                result = result - prev + (current - prev)
            else:
                result += current
        return result
