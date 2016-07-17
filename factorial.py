#!/usr/bin/env python3


def inputnumber():
    num = int(input('Enter number: '))
    return num


def factorial(num):
    factorial = 1
    while (num != 1):
        factorial *= num
        num -= 1
    return factorial


def main():
    a = inputnumber()
    b = factorial(a)
    print('Factorial of a %i is : %i' % (a, b))

if __name__ == '__main__':
    main()
