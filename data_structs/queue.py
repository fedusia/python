#!/usr/bin/env python3
''' Linear queue '''


class Queue:
    def __init__(self):
        self.items = list()

    def is_Empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def set(self, item):
        self.Queue.insert(0, item)

    def get(self):
        return self.items.pop()


def main():
    pass


if __name__ == '__main__':
    main()
