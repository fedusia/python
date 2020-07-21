# https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        left = 0
        while left < len(arr):
            if arr[left] == 0:
                arr.pop()
                arr.insert(left + 1, 0)
                left += 1
            left += 1


if __name__ == '__main__':
    test1 = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(test1)
    assert test1 == [1, 0, 0, 2, 3, 0, 0, 4]
