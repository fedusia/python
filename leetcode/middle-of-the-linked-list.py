#!/usr/bin/env python3
# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/

# Approach #1:
# Traverse the whole linked list and count the no. of nodes.
# Now traverse the list again till count/2 and return the node at count/2.

# Approach #2:
# Traverse linked list using two pointers. Move one pointer by one and the other pointers by two.
# When the fast pointer reaches the end slow pointer will reach the middle of the linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        counter = 0
        current = head
        while current is not None:
            counter += 1
            current = current.next

        if counter % 2 == 0:
            middleNode = counter // 2 + 1
        else:
            middleNode = counter // 2

        counter = 0
        while head is not None:
            counter += 1
            if counter == middleNode:
                return head
            head = head.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    h = Solution().middleNode(head)
    print(h)
