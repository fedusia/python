#!/usr/bin/env python

def check_uniq_symbols(string):
    hash_map = dict()
    for token in string:
        if hash_map.get(token):
            hash_map[token] += 1
            return False
        else:
            hash_map[token] = 1
    return True


if __name__ == '__main__':
    main()
