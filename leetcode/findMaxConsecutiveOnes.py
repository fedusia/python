# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3238/
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        prev = 0
        while left < len(nums):
            counter = 0
            if nums[left] == 1:
                right = left
                while right < len(nums):
                    if nums[right] == 1:
                        counter += 1
                        right += 1
                    else:
                        break
                right += 1
                left = right
            else:
                left += 1

            if counter > prev:
                prev = counter

        return prev


if __name__ == "__main__":
    assert Solution().findMaxConsecutiveOnes([0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]) == 6
    assert Solution().findMaxConsecutiveOnes([0, 1]) == 1
