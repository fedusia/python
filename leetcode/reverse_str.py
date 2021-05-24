#!/usr/bin/env/python3


def iterate_revert_string(s: list) -> list:
    """
    revert list iterate method
    """
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


def recursion_revert_string(s: list) -> list:
    """
    revert list elements recursion method
    """
    if len(s) == 0:
        return []
    return [s.pop()] + recursion_revert_string(s)

if __name__ == "__main__":
    t1 = ["f", "e", "d", "u", "s", "i", "a"]
    t2 = ["0", "q", " ", "1", "\\"]
    assert iterate_revert_string(t1), ["a", "i", "s", "u", "d", "e", "f"]
    assert recursion_revert_string(t1), ["a", "i", "s", "u", "d", "e", "f"]
    assert iterate_revert_string(t2), ["\\", "1", " ", "q", "0"]
    assert recursion_revert_string(t2), ["\\", "1", " ", "q", "0"]
