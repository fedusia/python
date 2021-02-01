#!/usr/bin/env python


def count(n):
    if len(n) <= 0:
        return 0
    elif len(n) == 1:
        return 1
    return 1 + count(n[1:])


def main():
    print(count([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
