#!/usr/bin/env python3

# Where to find explanation: https://www.geeksforgeeks.org/reverse-a-linked-list/
# Iterative approach:
# 1. Initialize three pointers prev as NULL, curr as head and next as NULL.
# 2. Iterate through the linked list. In loop, do following.
# 3. Before changing next of current,  store next node
# 4. Now change next of current, This is where actual reversing happens.
# 5. Move prev and curr one step forward

# Recursive approach:
# 1. Divide the list in two parts - first and rest
# 2. Call reverse to the rest list
# 3. Link rest to first.
# 4. Fix head pointer


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next is None or head is None:
            return head
        rest = Solution().reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest


class Solution:
    def iterative_reverse_list(self, head: ListNode) -> ListNode:
        prv = None
        next = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prv
            prv = cur
            cur = next
        head = prv
        return head


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    h = Solution().iterative_reverse_list(head)


if __name__ == "__main__":
    main()
