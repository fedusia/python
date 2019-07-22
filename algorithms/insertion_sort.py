#!/usr/bin/env python3

"""
    ** INSERTION SORT **
    Space compexity:
        - worst case: O(1)
    Time complexity:
        - worst case: O(n**2)
        - average case: O(n**2)
        - best case: O(n)
    Algorithm's steps:
        1. Select first unsorted element.
        2. Swap other elements to the right to create the correct position
            and shift the unsorted element
        3. Advance marker to the right one element
"""


def insertion_sort(A):
    for i in range(1, len(A)):
        k = A[i]
        j = i - 1
        while k < A[j] and j >= 0:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = k
    return A


def main():
    import random
    A = [random.randint(-100, 100) for _ in range(10)]
    print('Unsorted list: {}'.format(A))
    print('Sorted list: {}'.format(insertion_sort(A)))


if __name__ == '__main__':
    main()
