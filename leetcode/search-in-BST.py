# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return Solution().searchBST(root.left, val)
        else:
            return Solution().searchBST(root.right, val)


if __name__ == "__main__":
    root = TreeNode(
        18,
        left=TreeNode(
            2,
            left=None,
            right=None
        ),
        right=TreeNode(
            22,
            left=None,
            right=TreeNode(
                63,
                left=None,
                right=TreeNode(
                    84,
                    left=None,
                    right=None)
            ),
        ),
    )
    root = Solution().searchBST(root, 63)
    print(root.val)
