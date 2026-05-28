class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i,n in enumerate(s):
            if n in d1:
                d1[n]+=1
            else:
                d1[n]=1
        for i,n in enumerate(t):
            if n in d2:
                d2[n]+=1
            else:
                d2[n]=1
        if d1==d2:
            return True
        return False
    
        
        