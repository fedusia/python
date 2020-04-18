class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        i = 0
        output = 0
        while i < len(s):
            if i != 0 and symbols[s[i]] > symbols[s[i - 1]]:
                output += symbols[s[i]] - 2 * symbols[s[i - 1]]
            else:
                output += symbols[s[i]]
            i += 1
        return output


if __name__ == '__main__':
    assert Solution().romanToInt("MCMXCIV") == 1994
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IX") == 9
