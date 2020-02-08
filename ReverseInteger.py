import math
class Solution:
    def reverse(self, x: int) -> int:
        temp=abs(x)
        str_temp=list(str(temp))
        str_temp.reverse()
        str_temp=''.join(str_temp)
        if x<0:
            str_temp='-'+str_temp
        res=int(str_temp)
        if res<-math.pow(2,31) or res>math.pow(2,31)-1:
            res=0
        return res

s=Solution()
print(s.reverse(123))