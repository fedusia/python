class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        for char in strs[0]:
            prefix += char
            for word in strs:
                if prefix not in word:
                    prefix = prefix[:-1]
                    break
        return prefix


if __name__ == "__main__":
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix((["dog", "racecar", "car"])) == ""
