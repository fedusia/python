# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3237/
class Solution:
    def findNumbers(self, nums):
        i = 0
        result = 0
        while i < len(nums):
            digit = 0
            divider = 1
            while nums[i] // divider != 0:
                divider *= 10
                digit += 1
            if digit % 2 == 0:
                result += 1
            i += 1
        return result


if __name__ == '__main__':
    assert Solution().findNumbers([12, 345, 2, 6, 7896]) == 2
    assert Solution().findNumbers([555, 901, 482, 1771]) == 1
    assert Solution().findNumbers([437, 315, 322, 431, 686, 264, 442]) == 0
