class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = -1
        letters = "abcdefghijklmnopqrstuvwxyz"
        r = []
        while i < len(s):
            if s[i] == "#":
                print(s[i - 1 : i - 2])
                r.append(letters[int(s[i - 1 : i - 2])])
                i = i - 2
                continue
            r.append(letters[int(s[i])])
            i -= 1
        return r


if __name__ == "__main__":
    print(Solution().freqAlphabets("10#11#12"))
