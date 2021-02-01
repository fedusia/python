#!/usr/bin/env python


def mysum(n):
    if len(n) <= 0:
        return 0
    elif len(n) == 1:
        return n[0]
    return n[0] + mysum(n[1:])


def main():
    print(mysum([2, 4, 6, 10]))


if __name__ == "__main__":
    main()
