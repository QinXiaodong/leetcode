class Solution:
    


    def romanToInt(self, s: str) -> int:
        dict = {'I': 1,'II':2,'III':3,'IV':4,'V': 5,'VI':6,'VII':7,'VIII':8,'IX':9,\
            'X': 10,'XX':20,'XXX':30,'XL':40,'L': 50,'LX':60,'LXX':70,'LXXX':80,'XC':90,\
            'C': 100,'CC':200,'CCC':300,'CD':400,'D': 500,'DC':600,'DCC':700,'DCCC':800,'CM':900,\
            'M':1000,'MM':2000,'MMM':3000}
        res=0
        while len(s)>0:
            if s in dict:
                res+=dict[s]
                break
            i=1
            while s[:i] in dict:
                i+=1
            res+=dict[s[:i-1]]
            s=s[i-1:]
        return res

s=Solution()
print(s.romanToInt('MCMXCIV'))