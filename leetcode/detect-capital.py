#!/usr/bin/env python3


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for char in word:
            if char.isupper():
                count += 1

        if count == len(word) or count == 0 or (count == 1 and word[0].isupper()):
            return True
        return False


if __name__ == "__main__":
    assert Solution().detectCapitalUse("USA") == True
    assert Solution().detectCapitalUse("Yandex") == True
    assert Solution().detectCapitalUse("myCustomstring") == False
    assert Solution().detectCapitalUse("leetcode") == True
