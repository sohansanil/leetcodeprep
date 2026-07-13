# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def countPaths(node, remaining):

            if not node:
                return 0

            count = 0

            if node.val == remaining:
                count = 1

            count += countPaths(node.left, remaining - node.val)
            count += countPaths(node.right, remaining - node.val)

            return count


        def dfs(node):

            if not node:
                return 0

            return (
                countPaths(node, targetSum)
                + dfs(node.left)
                + dfs(node.right)
            )

        return dfs(root)