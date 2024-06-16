#!/usr/bin/python3
"""Finds the longest substring in a given string
withoit repeating characters"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx_map = {}
        _max = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_idx_map and char_idx_map[s[end]] >= start:
                start = char_idx_map[s[end]] + 1

            char_idx_map[s[end]] = end

            _max = max(_max, (end - start) + 1 )

        return _max
