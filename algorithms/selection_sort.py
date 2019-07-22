#!/usr/bin/env python3

"""
    ** SELECTION SORT **
    Space complexity:
        - worst case: O(1)
    Time complexity:
        - worst case: O(n**2)
        - average case: O(n**2)
        - best case: O(n**2)
    Algorithm's steps:
    1. Find the smallest element. Swap it with the first element.
    2. Find the second smallest element. Swap it with the second element
    3. Find the third smallest element. Swap it with the third element
    4. Repeat finding the smallest element and swapping in the correct position until the list is sorted
"""


def main():
    import random
    A = [random.randint(-100, 100) for _ in range(10)]
    print('Unsorted list: {}'.format(A))
    print('Sorted list: {}'.format(selection_sort(A)))


def selection_sort(A):
    i = 0
    j = i
    while i < len(A) - 1:
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
        if j < len(A) - 1:
            j += 1
        else:
            i += 1
            j = i
    return A


if __name__ == '__main__':
    main()
