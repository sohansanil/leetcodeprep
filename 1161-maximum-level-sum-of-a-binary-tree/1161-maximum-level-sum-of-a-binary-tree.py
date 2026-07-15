# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])

        max_level_sum = float('-inf')
        answer = 1
        level = 1

        while q:

            size = len(q)
            level_sum = 0

            for i in range(size):

                node = q.popleft()

                level_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if level_sum > max_level_sum:
                max_level_sum = level_sum
                answer = level

            level += 1

        return answer