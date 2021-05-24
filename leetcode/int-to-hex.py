class Solution:
    def toHex(self, num: int) -> str:
        hex_digits = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f",
        }
        p, r = divmod(num, 16)
        s = list()
        s.append(hex_digits[r])
        while p > 0:
            r = p % 16
            s += hex_digits[r]
            p = p // 16
        return s[::-1]


if __name__ == "__main__":
    Solution().toHex(2037)
