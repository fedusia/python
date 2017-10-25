#!/usr/bin/env python3


# # Bad example
# def main():
#     a = int(input())
#     if -15 < a <= 12:
#         print(True)
#     elif 14 < a < 17:
#         print(True)
#     elif a >= 19:
#         print(True)
#     else:
#         print(False)


# Good example:
def main():
    a = int(input())
    print(-15 < a <= 12 or 14 < a < 17 or 19 <= a)


if __name__ == '__main__':
    main()
