class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:



        res=[]
        curr=[]
        nums.sort()
        memory=set()


        def dfs(i):
            if i==len(nums):
                if curr not in res:
                    res.append(curr.copy())
                    

                return
            curr.append(nums[i])
            dfs(i+1)
            
            curr.pop()
            dfs(i+1)
        dfs(0)
        return res
            
        