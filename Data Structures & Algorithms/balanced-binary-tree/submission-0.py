# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_balanced = True
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if abs(left - right) > 1:
            return float('inf')
        return 1 + max(left, right)
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) != float('inf')
