from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, node: 'Node', result: List[int]) -> 'Node':
        if not node:
            return node
        result.append(node.val)
        for child in node.children:
            self.dfs(child, result)