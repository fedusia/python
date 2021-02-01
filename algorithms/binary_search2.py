#!/usr/bin/env python2


def binary_search(sorted_list, element):
    # Работеет на сортированном списке.
    # на вход получает сортированный список и элемент для поиска
    # возвращает позицию в сортированном списке найденного элемента или None
    # Алгоритм:
    # 1. Выбираем центральный элемент
    # 2. Если он равен искомому элементу, возвращаем индекс элемента.
    # 3. Если он больше искомого двигаем правую границу в центр
    # 4. Если он меньше двигаем левую границу в центр
    left = 0
    right = len(sorted_list) - 1
    while left < right:
        mid = (left + right) // 2
        cur_element = sorted_list[mid]
        if cur_element == element:
            return mid
        if cur_element > element:
            right = mid - 1
        else:
            left = mid + 1


def main():
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))


if __name__ == "__main__":
    main()
