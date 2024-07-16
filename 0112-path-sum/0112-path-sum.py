# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def depthFirstSearch(root,currentSum):
            if not root:
                return False
            currentSum += root.val
            if not root.left and not root.right:
                return currentSum == targetSum
            
            return (depthFirstSearch(root.left,currentSum) or depthFirstSearch(root.right,currentSum))
        return depthFirstSearch(root,0)