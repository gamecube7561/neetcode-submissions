# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([])
        queue.append(root)
        res = []
        res.append([root.val])

        while queue or temp_queue:
            temp_queue = []
            while queue:
                node = queue.popleft()
                if node.left:
                    temp_queue.append(node.left)
                if node.right:    
                    temp_queue.append(node.right)
            res.append([n.val for n in temp_queue])
            queue.extend(temp_queue)
        return res[0:-1]