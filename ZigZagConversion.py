class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or numRows==1:
            return s
        res=''
        i=0
        #处理第一行
        while i<len(s):
            res+=s[i]
            i+=numRows*2-2
        #处理中间行
        for i in range(1,numRows-1):
            j=i
            while j<len(s):
                res+=s[j]
                if j+(numRows-i-1)*2<len(s):
                    res+=s[j+(numRows-i-1)*2]
                j+=(numRows-1)*2
        #处理最后一行
        i=numRows-1
        while i<len(s):
            res+=s[i]
            i+=numRows*2-2
        return res
            




s=Solution()
print(s.convert('AB',1))