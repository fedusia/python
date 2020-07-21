class Solution:
    def sortedSquares(self, A):
        nums = [num ** 2 for num in A]
        nums.sort()
        return nums


if __name__ == '__main__':
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
