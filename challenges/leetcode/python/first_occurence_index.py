#!/usr/bin/python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        try:
            while haystack[i]:
                temp = haystack[i:]
                if temp.startswith(needle):
                    return i
                i += 1
        except IndexError:
            return -1
