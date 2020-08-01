class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brakets = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in ["{", "(", "["]:
                st.append(i)
            elif st and i == brakets[st[-1]]:
                st.pop()
            else:
                return False
        return st == []



if __name__ == "__main__":
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("{[]}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("]") is False
    assert Solution().isValid("(])") is False
