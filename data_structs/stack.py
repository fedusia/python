#!usr/bin/env python3


def main():
    input_data = input()
    print(check(input_data))


def check(input_data):
    stack = Stack()
    i = 0
    while i < len(input_data):
        if input_data[i] == '(' :
            stack.push('(')
        elif input_data[i] == ')' and not stack.empty():
            stack.pop()
        i += 1
    # import ipdb; ipdb.set_trace()
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
