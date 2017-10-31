#!/usr/bin/env python3

import timeit


def binary_search(target, sequence):
    lo = 0
    hi = len(sequence)
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] == target:
            return '{} found in sequence'.format(mid)
        elif sequence[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1


def operator_in(target, sequence):
    return target if target in sequence else None


def main():
    t1 = timeit.timeit('binary_search(target, sequence)',
                       setup='from __main__ import binary_search;'
                             'target = 1999; sequence = [i for i in range(2000)]'
                       )
    t2 = timeit.timeit('operator_in(target, sequence)',
                       setup='from __main__ import operator_in;'
                             'target = 1999; sequence = [i for i in range(2000)]'
                       )

    print('binary_search: {}'.format(t1))
    print('operator_in: {}'.format(t2))


if __name__ == '__main__':
    main()
