#!/usr/bin/env python3


def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[j], nums[min_idx] = nums[min_idx], nums[j]
    return nums


if __name__ == "__manin__":
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
