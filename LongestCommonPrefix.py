from typing import List
class Solution:
    def LCP(self,a:str,b:str)->str:
        res=''
        for i in range(min(len(a),len(b))):
            if a[i]!=b[i]:
                break
            res+=a[i]
        return res
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp=strs[0]
        for i in range(1,len(strs)):
            temp=self.LCP(temp,strs[i])
            if temp=='':
                return temp
        return temp
s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))