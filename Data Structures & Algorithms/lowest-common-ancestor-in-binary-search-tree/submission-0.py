# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def get_node(root, target, seen):
            if not root:
                return []
            seen.append((root, root.val))
            if target == root.val:
                return seen
            elif root.val > target:
                return get_node(root.left, target, seen)
            elif root.val < target:
                return get_node(root.right, target, seen)

        q_nodes = get_node(root, p.val, [])
        p_nodes = get_node(root, q.val, [])

        while q_nodes:
            node, val = q_nodes.pop()
            if (node, val) in p_nodes:
                return node
        return root
            
        