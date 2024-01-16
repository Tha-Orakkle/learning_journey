#!/usr/bin/python3
"""Creates  pascal triangle"""

class Solution:
    def generate(self, numRows):
        """generates the triangle"""
        triangle = []
        for i in range(numRows):
            row = [1]
            if triangle:
                last_row = triangle[-1]
                row.extend(sum(pair) for pair in zip(last_row, last_row[1:]))
                row.append(1)
            triangle.append(row)
        return triangle

if __name__ == "__main__":
    tri = Solution()
    print(tri.generate(5))
