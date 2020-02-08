class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict={}
        e=0
        start=0
        res=0
        while e < len(s):
            if s[e] in mydict:
                start=max(start,mydict[s[e]]+1)
            mydict[s[e]]=e
            res=max(res,e-start+1)
            e+=1
        return res

s=Solution()
print(s.lengthOfLongestSubstring("abba"))