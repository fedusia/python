#!/usr/bin/env python3
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/


class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda n: bin(n).count("1"))


if __name__ == "__main__":
    assert Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [
        0,
        1,
        2,
        4,
        8,
        3,
        5,
        6,
        7,
    ]
    assert Solution().sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [
        1,
        2,
        4,
        8,
        16,
        32,
        64,
        128,
        256,
        512,
        1024,
    ]
