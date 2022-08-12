from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.parent_dict = {}

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.init_parent(root)


    def init_parent(self, root: Optional[TreeNode]):
        if not root:
            return
        if root.left:
            self.parent_dict[root.left] = root
            self.init_parent(root.left)
        if root.right:
            self.parent_dict[root.right] = root
            self.init_parent(root.right)
