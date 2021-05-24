#!/usr/bin/env python3
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp = head
        head = head.next
        tmp.next = head.next
        head.next = tmp
        if head.next.next is None:
            return head
        head.next.next = Solution().swapPairs(head.next.next)
        return head


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    h = Solution().swapPairs(head)
    result = []
    while h:
        result.append(h.val)
        h = h.next
    return result


if __name__ == "__main__":
    assert main() == [2, 1, 4, 3]
