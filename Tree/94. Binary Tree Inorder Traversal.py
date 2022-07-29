from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        values = []
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            values.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return values

if __name__ == '__main__':
    Solution().inorderTraversal()