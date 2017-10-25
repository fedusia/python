#!/usr/bin/env python3


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2

    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    print(s)


if __name__ == '__main__':
    main()
