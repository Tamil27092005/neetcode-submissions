class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        else:
            dt=[]
            for i in s:
                dt.append(i)
            for i in range(len(dt)):
                temp=dt[:i]+dt[i+1:]
                if temp==temp[::-1]:
                    return True
            else:
                return False
                    
