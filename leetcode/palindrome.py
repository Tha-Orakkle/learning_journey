#!/usr/bin/python3
"""checks if an integer is a palindrome
and returns true or false"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)[::-1]
        if temp[-1] == "-":
            return False
        if int(temp) == x:
            return True
        else:
            return False


if __name__ == "__main__":
    x = int(input("Enter a Number:\n"))
    test = Solution()
    print(test.isPalindrome(x))
