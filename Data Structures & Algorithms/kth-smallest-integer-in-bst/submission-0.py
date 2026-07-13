# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        order=[]
        curr=root
        while  stack or curr:
            while curr:
                
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            order.append(curr)
            curr=curr.right
        node=order[k-1]
        return node.val
            
        
        