import string
import timeit
import pytest
from memory_profiler import profile


# @profile
def f(palindrom):
    i = 0
    j = -1
    strings = set(string.ascii_letters)
    while i < len(palindrom)/2:
        if palindrom[i] not in strings:
            i += 1
            continue
        if palindrom[j] not in strings:
            j -= 1
            continue
        if palindrom[i].lower() != palindrom[j].lower():
            return False
        i += 1
        j -= 1
    return True


def test_f_palidrom_word():
    s = 'Madam'
    assert f(s) is True


def test_f_not_palidrom_word():
    s = 'fedusia'
    assert f(s) is False


def test_f_palidrom_sentence():
    s = 'Mr. Owl ate my metal worm.'
    assert f(s) is True


def test_f_palindrom2_sentence():
    s = "Mother Eve's noose we soon sever, eh, Tom?"
    assert f(s) is True


def test_f_palindrom4_sentence():
    s = "Saladin enrobes a baroness, Senora, base-born Enid, alas."
    assert f(s) is True


def test_f_not_palindrom_sentence():
    s = 'Mr. OwQWQWqasl ate my metal worm.'
    assert f(s) is False


# @profile
def f1(palindrom):
    i = 0
    j = -1
    strings = string.ascii_letters
    while i < len(palindrom)/2:
        if palindrom[i] not in strings:
            i += 1
            continue
        if palindrom[j] not in strings:
            j -= 1
            continue
        if palindrom[i].lower() != palindrom[j].lower():
            return False
        i += 1
        j -= 1
    return True


def test_f1_palidrom_word():
    s = 'Madam'
    assert f(s) is True


def test_f1_not_palidrom_word():
    s = 'fedusia'
    assert f1(s) is False


def test_f1_palidrom_sentence():
    s = 'Mr. Owl ate my metal worm.'
    assert f1(s) is True


def test_f1_palindrom2_sentence():
    s = "Mother Eve's noose we soon sever, eh, Tom?"
    assert f1(s) is True


def test_f1_palindrom4_sentence():
    s = "Saladin enrobes a baroness, Senora, base-born Enid, alas."
    assert f1(s) is True


def test_f1_not_palindrom_sentence():
    s = 'Mr. OwQWQWqasl ate my metal worm.'
    assert f1(s) is False


# @profile
def f2(s):
    s = ''.join([c for c in s.lower() if 97 <= ord(c) <= 122])
    return s == s[::-1]


if __name__ == '__main__':
    s = 100000 * 'Mr. Owl ate my metal worm.'
    t = timeit.Timer(lambda: f(s))
    t1 = timeit.Timer(lambda: f1(s))
    t2 = timeit.Timer(lambda: f2(s))
    print('t with search in set: {}'.format(t.timeit(number=10)))
    print('t1 with search in list: {}'.format(t1.timeit(number=10)))
    print('t2 with : {}'.format(t2.timeit(number=10)))
