#!/usr/bin/env python3

def bubble_sort(nums):
    for _ in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

if __name__ == "__main__":
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 0]) == [0, 2, 3, 4, 5]
