# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.pre_value = -pow(2, 31)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        is_left_valid = self.isValidBST(root.left)
        is_right_valid = self.isValidBST(root.right)
        if root.val <= self.pre_value:
            return False
        else:
            self.pre_value = root.val
        return is_left_valid and is_right_valid

if __name__ == '__main__':
    print(-pow(2, 31))
    node = []
    node.pop(0)