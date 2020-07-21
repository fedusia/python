# https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums1):
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
        else:
            nums1.extend(nums2[j:])
        # print(nums1)


if __name__ == '__main__':
    assert Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
