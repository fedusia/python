#!/usr/bin/env python3


# Task #3
def main():
    a, b = float(input()), float(input())
    operator = input()
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else 'Деление на 0!',
        'mod': lambda x, y: x % y if y != 0 else 'Деление на 0!',
        'pow': lambda x, y: x ** y,
        'div': lambda x, y: x // y if y != 0 else 'Деление на 0!'
    }

    print('{}'.format(ops[operator](a, b)))


if __name__ == '__main__':
    main()
