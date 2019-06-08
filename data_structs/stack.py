#!usr/bin/env python3


def main():
    input_data = input()
    print(check(input_data))


def check(input_data):
    stack = Stack()
    for char in input_data:
        if char in ['[', '{']:
            stack.push(char)
        else:
            if stack.empty():
                return False
            top = stack.top()
            if top == '[' and char != ']' or\
               top == '{' and char != '}':
                return False
            stack.pop()
    return stack.empty()


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        if len(self.stack):
            return False
        return True

if __name__ == '__main__':
    main()
