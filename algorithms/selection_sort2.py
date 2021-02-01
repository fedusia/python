#!/usr/bin/env python

# Сортировка выбором
# Алгоритм:
# состоит из 2 этапов:
# найти наименьшеий элемент
# удалить из текущего массива и вставить в новый сортированный.
# Сложность алгоритма O(n2) так как есть операция поиска минимум O(n) и ее выполняем n раз


def find_min(arr):
    min_element = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
            min_index = i

    return min_index


def find_max(arr):
    max_element = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i

    return max_index


def selection_sort(arr):
    new_array = []
    for i in range(len(arr)):
        min_elem = find_min(arr)
        new_array.append(arr.pop(min_elem))
    return new_array


def main():
    print(selection_sort([55, 3, 45, 5, 6, 5, 4, 2]))


if __name__ == "__main__":
    main()
