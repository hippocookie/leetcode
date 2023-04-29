from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start, end):
            result = []
            if start > end:
                result.append(None)
                return result

            for i in range(start, end + 1):
                left_tree = generate_trees(start, i - 1)
                right_tree = generate_trees(i + 1, end)

                for left in left_tree:
                    for right in right_tree:
                        curt = TreeNode(i)
                        curt.left = left
                        curt.right = right
                        result.append(curt)
            return result
        return generate_trees(1, n) if n else []

    # overtime
    def numTrees(self, n: int) -> int:
        def num_trees(start, end):
            if start > end:
                return [None, ]
            trees = []
            for i in range(start, end + 1):
                left_tree = num_trees(start, i - 1)
                right_tree = num_trees(i + 1, end)

                for left in left_tree:
                    for right in right_tree:
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees
        return len(num_trees(1, n)) if n else 0

    def numTrees2(self, n: int) -> int:
        num = [0] * (n + 1)
        num[0], num[1] = 1, 1

        for j in range(2, n + 1):
            for k in range(1, j + 1):
                num[j] += num[k - 1] * num[j - k]
        return num[n]


if __name__ == '__main__':
    result = Solution().numTrees2(3)
    print(result)