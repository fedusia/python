#!/usr/bin/env python

def check_uniq_symbols(my_string):
    hash_map = dict()
    for token in my_string:
        if hash_map.get(token):
            hash_map[token] += 1
            return False
        else:
            hash_map[token] = 1
    return True


def main():
    print(check_uniq_symbols(raw_input()))


if __name__ == '__main__':
    main()
