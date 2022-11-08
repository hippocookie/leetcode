from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            row = []
            while queue:
                node = queue.pop(0)
                row.append(node)
            result.append([n.val for n in row])
            for node in row:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result