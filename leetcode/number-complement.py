# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/


class Solution:
    def findComplement(self, num):
        x = bin(num)
        binary = 0
        for i in range(len(x[2:])):
            binary = binary ^ (1 << i)
        print(binary)


if __name__ == "__main__":
    Solution().findComplement(5)
