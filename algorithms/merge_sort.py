#!/usr/bin/env python


def main():
    a = [1, 100, 10, 8, 1000, 333]
    print("result: {}".format(merge_sort(a)))


def merge_sort(A):
    if len(A) == 1:
        return A
    middle = len(A) // 2
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left, right)


def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


if __name__ == "__main__":
    main()
