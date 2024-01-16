#!/usr/bin/python3
"""finds the square root without usimg the
'**' operator"""

class Solution:
    def mySqrt(self, x):
        """finds square root"""
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        guess = x / 2.0
        for _ in range(20):
            guess = 0.5 * (guess + x / guess)

        return guess

if __name__ == "__main__":
    a = Solution()
    n = int(input("Enter a number: "))
    print(a.mySqrt(n))
