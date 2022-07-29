from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        values = []
        stack = [root]
        reverse_stack = []
        while stack:
            node = stack.pop()
            reverse_stack.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while reverse_stack:
            values.append(reverse_stack.pop().val)
        return values


if __name__ == '__main__':
    Solution().postorderTraversal()
