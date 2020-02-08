class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
s=Solution()
print(s.isPalindrome(1211))