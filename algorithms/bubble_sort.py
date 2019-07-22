#!/usr/bin/env python3


def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


def main():
    import random
    A = [random.randint(-100, 100) for _ in range(10)]
    print('Unsorted list: {}'.format(A))
    print('Sorted list: {}'.format(bubble_sort(A)))


if __name__ == '__main__':
    main()
