class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        

        def dfs(sum,curr,i):
            if sum==target:
                res.append(curr.copy())
                return 
            if i>=len(nums) or sum>target:
                return
            curr.append(nums[i])
            dfs(sum+nums[i],curr,i)
            curr.pop()
            dfs(sum,curr,i+1)
        dfs(0,[],0)
        return res


            
        