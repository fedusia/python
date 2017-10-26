#!/usr/bin/env python3


def main():
    a = list(input())
    if (sum(map(int, a[:3])) == sum(map(int, a[3:]))):
        print('Счастливый')
    else:
        print('Обычный')


if __name__ == '__main__':
    main()