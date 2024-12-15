# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val == 1

        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)

        if root.val == 2:  # OR 
            return left_result or right_result
        elif root.val == 3:  # AND 
            return left_result and right_result

        
    

        
        