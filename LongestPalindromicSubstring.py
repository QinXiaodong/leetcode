import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=np.zeros((len(s),len(s)+1))
        st=0
        ed=0
        for i in range(len(s)):
            dp[i][1]=1
            if i<len(s)-1 and s[i]==s[i+1]:
                dp[i][2]=1
                st=i
                ed=i+1
        for j in range(3,len(s)+1):
            for i in range(len(s)-j+1):
                if s[i]==s[i+j-1] and dp[i+1][j-2]==1:
                    dp[i][j]=1
                    if j>ed-st:
                        ed=i+j
                        st=i
        return s[st:ed]


s=Solution()
print(s.longestPalindrome('cbbd'))