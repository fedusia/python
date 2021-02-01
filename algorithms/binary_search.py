#!/usr/bin/env python3

import timeit

"""
    Algorithm  steps:
    0. Find mid element.
    1. Compare target with the middle element.
    2. If target matches with middle element, we return the mid index.
    3. Else If target is greater than the mid element, then target can only
        lie in right half subarray after the mid element.
        So we recur for right half.
    4. Else (target is smaller) recur for the left half.

"""


def binary_search(target, sequence):
    lo = 0
    hi = len(sequence)
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] == target:
            return "Found in sequence at index {}".format(mid)
        elif sequence[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1


def operator_in(target, sequence):
    return target if target in sequence else None


def main():
    t1 = timeit.timeit(
        "binary_search(target, sequence)",
        setup="from __main__ import binary_search;"
        "target = 20000000; sequence = [i for i in range(20000001)]",
        number=100
    )
    t2 = timeit.timeit(
        "operator_in(target, sequence)",
        setup="from __main__ import operator_in;"
        "target = 20000000; sequence = [i for i in range(20000001)]",
        number=100
    )

    print("binary_search: {}".format(t1))
    print("operator_in: {}".format(t2))


if __name__ == "__main__":
    main()
