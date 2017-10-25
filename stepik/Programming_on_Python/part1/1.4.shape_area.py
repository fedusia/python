#!/usr/bin/env python3


def main():
    shape = input()
    if shape == 'прямоугольник':
        a, b = int(input()), int(input())
        print('{}'.format(a * b))
    if shape == 'треугольник':
        a, b, c = int(input()), int(input()), int(input())
        p = (a + b + c) / 2
        print('{}'.format((p * (p - a) * (p - b) * (p - c)) ** (1/2)))
    if shape == 'круг':
        r = int(input())
        pi = 3.14
        print('{}'.format(pi * r ** 2))


if __name__ == '__main__':
    main()
