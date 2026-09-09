class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin,curmax=1,1
        res=max(nums)
        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            temp=curmax*n
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(temp,curmin*n,n)
            res=max(res,curmax,curmin)
        return res