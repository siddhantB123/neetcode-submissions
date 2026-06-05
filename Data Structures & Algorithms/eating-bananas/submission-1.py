class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## 0,1.... max(piles)
        l=1
        r=max(piles)
        mink=r
        while l<=r:
            k= l+(r-l)//2
            sum=0
            for i,n in enumerate(piles):
                sum+=math.ceil(n/k)
                
            if sum<=h:
                r=k-1
                mink=min(mink,k)
            else:
                l=k+1
        return mink


        
        