class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(filter(lambda ch: ch.isalnum() , s))
        l=len(s1)

        

        s1=s1.upper()

        for i in range(0,len(s1)//2):
            if s1[i]!=s1[l-1-i]:
                print(s[i],i)
                return False
        return True


        