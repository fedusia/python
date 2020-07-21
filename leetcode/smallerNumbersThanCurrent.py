# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        i = 0
        result = []
        while i < len(nums):
            c = 0
            j = 0
            while j < len(nums):
                if nums[i] > nums[j]:
                    c += 1
                j += 1
            result.append(c)
            i += 1
        return result


if __name__ == '__main__':
    assert Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
    assert Solution().smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]
    assert Solution().smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]
