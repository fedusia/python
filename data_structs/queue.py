#!/usr/bin/env python3
''' Linear queue '''


class Queue:
    def __init__(self, items=[]):
        self.items = items

    def is_Empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


def main():
    pass


if __name__ == '__main__':
    main()
