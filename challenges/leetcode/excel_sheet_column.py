#!/usr/bin/python3
"""USing Python to implement the excel sheet column"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while (columnNumber > 0):
            columnNumber -= 1

            rem = columnNumber % 26
            result = chr(ord('A') + rem) + result

            columnNumber //= 26

        return result

if __name__ == "__main__":
    test = Solution()
    print(test.convertToTitle(30))
