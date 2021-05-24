#!/usr/bin/env python
import timeit

def quick_sort(N):
    if len(N) < 2:
        return N
    else:
        # worst case
        pivot = N[0]
        # best case == middle case
        # pivot = N[len(N)//2]
        # pivot_index = len(N)//2
        less = []
        greater = []
        for i in range(len(N)):
            # if i == pivot_index:
            #     continue
            if N[i] <= pivot:
                less.append(N[i])
            else:
                greater.append(N[i])

        return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    print(quick_sort([100, 23, 2, 1, 233, 0, 333, 333]))

    t1 = timeit.timeit(
        "quick_sort(sequence)",
        setup="from __main__ import quick_sort; import random;"
        "sequence = [random.randint(0,100) for i in range(100)]",
        number=100,
    )
    t2 = timeit.timeit(
        "quick_sort(sequence)",
        setup="from __main__ import quick_sort; import random;"
        "sequence = [random.randint(0,100) for i in range(1000)]",
        number=100,
    )
    t3 = timeit.timeit(
        "quick_sort(sequence)",
        setup="from __main__ import quick_sort; import random;"
        "sequence = [random.randint(0,100) for i in range(10000)]",
        number=100,
    )
    # t4 = timeit.timeit(
    #     "quick_sort(sequence)",
    #     setup="from __main__ import quick_sort; import random;"
    #     "sequence = [random.randint(0,100) for i in range(100000)]",
    #     number=100,
    # )
    print("100: {}".format(t1))
    print("1000: {}".format(t2))
    print("10000: {}".format(t3))
    #print("100000: {}".format(t4))


if __name__ == "__main__":
    main()
