#!usr/bin/env python3


def main():
    input_data = input()
    print(check(input_data))


def check(input_data):
    stack = Stack()
#     import ipdb; ipdb.set_trace()
    for idx, char in enumerate(input_data):
        if char in ['[', '{', '(']:
            stack.push(char)
        elif char in [']', '}', ')']:
            if stack.empty():
                return idx + 1
            top = stack.top()
            if top == '[' and char != ']' or\
               top == '{' and char != '}' or\
               top == '(' and char != ')':
                return idx + 1
            stack.pop()
        else:
            continue
    if stack.empty():
        return 'Success'
    return len(stack.stack)


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
