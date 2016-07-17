#!/usr/bin/env python3


def inputNumber():
    counter = 0
    numbers = list()
    while True:
        num = int(input('Enter number:'))
        if isinstance(num, int):
            numbers.append(num)
            counter += 1
        else:
            print ('Not number: %s' % num)
            continue
        if counter == 3:
            break
    return numbers


def max(list):
    max = sorted(list, reverse=True)
    return max[0]


def main():
    a = inputNumber()
    b = max(a)
    print('Max of 3 digits %s is: %i' % (a, b))

if __name__ == '__main__':
    main()
