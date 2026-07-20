class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        

        def dfs(sum,curr,i):
            if sum==target :
                res.append(curr.copy())
                return 
            if i>=len(nums) or sum>target:
                return
            curr.append(nums[i])
            dfs(sum+nums[i],curr,i+1)
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(sum,curr,i+1)
        dfs(0,[],0)
        return res
        
        