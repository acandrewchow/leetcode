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

    # def evaluateTree(self, root: Optional[TreeNode]) -> bool:
    #     stack = [root]
    #     value = {} # map node -> value

    #     while stack:
    #         node = stack.pop()
    #         # leaf node
    #         if not node.left:
    #             value[node] = node.val == 1
    #         # non-leaf node
    #         else:
    #             if node.left in value:
    #                 if node.val == 2:
    #                     value[node] = value[node.left] or value[node.right]
    #                 if node.val == 3:
    #                      value[node] = value[node.left] and value[node.right]
    #             # otherwise add children
    #             else:
    #                 stack.extend([node, node.left, node.right])
    #     return value[root]

        
    

        
        