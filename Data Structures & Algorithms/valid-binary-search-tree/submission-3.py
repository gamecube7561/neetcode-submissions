# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def helper(node, min_val, max_val):
            if not node:
                return True

            if node.val > min_val and node.val < max_val:
                return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)

            return False
            

        return helper(root.left, float('-inf'), root.val) and helper(root.right, root.val, float('inf'))
        