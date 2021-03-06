#!/usr/bin/env python3
""" Linear queue """


class Queue:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


def main():
    pass


if __name__ == '__main__':
    main()
