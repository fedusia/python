class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1

        if x > 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        tmp = 0
        while x % 10 != 0 or x // 10 != 0:
            x, r = divmod(x, 10)
            tmp = tmp * 10 + r

        if abs(tmp) > max_int:
            return 0
        return tmp * sign


if __name__ == '__main__':
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321