#!/usr/bin/env python


def quick_sort(N):
    if len(N) < 2:
        return N
    else:
        pivot = N[0]
        less = []
        greater = []
        for i in N[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)

        return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    print(quick_sort([100, 23, 2, 1, 233, 0, 333, 333]))


if __name__ == "__main__":
    main()
