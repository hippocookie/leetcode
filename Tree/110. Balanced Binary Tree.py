# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Result:
    def __init__(self, is_balanced: bool, height: int):
        self.height = height
        self.is_balanced = is_balanced

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkBst(root).is_balanced

    def checkBst(self, root: Optional[TreeNode]) -> Result:
        if not root:
            return True
        left = self.checkBst(root.left)
        right = self.checkBst(root.right)
        return Result(left.is_balanced and right.is_balanced and abs(left.height - right.height) <= 1, max(left.height, right.height))

