#!/usr/bin/env python3

import time
from random import randrange


def findMinOn2(nlist):
    start = time.time()
    minimum = nlist[0]
    for i in nlist:
        issmallest = True
        for j in nlist:
            if i > j:
                issmallest = False
        if issmallest:
            minimum = i
    end = time.time()
    return minimum, end - start


def findMinOn(nlist):
    start = time.time()
    minimum = nlist[0]
    for i in nlist:
        if i < minimum:
            minimum = i
    end = time.time()
    return minimum, end - start


def main():
    for listSize in range(1000, 10001, 1000):
        nlist = [randrange(100000) for x in range(listSize)]
        start = time.time()
        print(findMinOn2(nlist))
        end = time.time()
        print("size: %d time: %f" % (listSize, end-start))

if __name__ == '__main__':
    main()
