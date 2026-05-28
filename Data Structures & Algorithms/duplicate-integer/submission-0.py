class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i,n in enumerate(nums):
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        for i in count.values():
            if i>1:
                return True
        return False
        