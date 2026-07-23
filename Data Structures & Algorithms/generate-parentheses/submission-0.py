class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def dfs(closeN,openN):
            if closeN==openN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                dfs(closeN,openN+1)
                stack.pop()
            if closeN<openN:
                stack.append(")")
                dfs(closeN+1,openN)
                stack.pop()
        dfs(0,0)
        return res
        
        