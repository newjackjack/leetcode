from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    # swap the left child and right child using the waterfall swaping method
    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)

    return root


tree_1 = [4, 2, 7, 1, 3, 6, 9]
expected_tree_1 = [4, 7, 2, 9, 6, 3, 1]
print(invertTree(tree_1))
