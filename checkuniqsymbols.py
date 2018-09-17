def check_uniq_symbols(string):
    hash_map = dict()
    for token in string:
        if hash_map.get(token):
            hash_map[token] += 1
            return False
        else:
            hash_map[token] = 1
    return True
