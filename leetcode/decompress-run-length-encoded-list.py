# https://leetcode.com/problems/decompress-run-length-encoded-list/


class Solution:
    def decompressRLElist(self, nums):
        i = 0
        result = []
        while i < len(nums):
            freq, val = nums[i], nums[i + 1]
            result.extend([val] * freq)
            i += 2
        return result


if __name__ == "__main__":
    assert Solution().decompressRLElist([1, 2, 3, 4]) == [2, 4, 4, 4]
    assert Solution().decompressRLElist([1, 1, 2, 3]) == [1, 3, 3]
