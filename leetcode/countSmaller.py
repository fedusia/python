# https://leetcode.com/problems/count-of-smaller-numbers-after-self/


class Solution:
    # построить bst и количество левых узлов в кажом поддереве это и будет кол-во элементов меньше этого числа
    def countSmaller(self, nums):
        i = 0
        result = []
        while i < len(nums):
            c = 0
            j = i
            while j < len(nums):
                if nums[i] > nums[j]:
                    c += 1
                j += 1
            result.append(c)
            i += 1
        return result


if __name__ == "__main__":
    import timeit

    with open("data_countSmaller", "r") as f:
        data = f.readline().split(",")
        data = list(map(int, data))
        t = timeit.Timer(Solution().countSmaller(data))
        print(t.timeit(number=1))

    assert Solution().countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
