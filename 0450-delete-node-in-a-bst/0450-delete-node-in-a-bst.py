# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Didn't find the node
        if not root:
            return None

        # Search left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Found the node
        else:

            # No left child
            if not root.left:
                return root.right

            # No right child
            if not root.right:
                return root.left

            # Two children:
            # Find smallest node in right subtree
            smallest = root.right

            while smallest.left:
                smallest = smallest.left

            # Copy its value into current node
            root.val = smallest.val

            # Delete the original copy
            root.right = self.deleteNode(root.right, smallest.val)

        return root

        