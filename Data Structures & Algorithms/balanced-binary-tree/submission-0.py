# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr:Optional[TreeNode])->int:
            if curr is None:
                return 0



            left=dfs(curr.left)
            right=dfs(curr.right)
            return 1+max(left,right)
        if root is None:
            return True
        stack=[root]
        while stack:
            node=stack.pop()
            if abs(dfs(node.left)-dfs(node.right))>1:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True

        
        