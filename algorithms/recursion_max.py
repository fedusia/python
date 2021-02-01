#!/usr/bin/env python


def maximum(n):
    if len(n) <= 0:
        return 0
    if len(n) == 1:
        return n[0]

    m = n[0]
    t = maximum(n[1:])
    if m < t:
        m = t
    return m


def main():
    print(maximum([123, 555, 1, 333, 112]))


if __name__ == "__main__":
    main()
