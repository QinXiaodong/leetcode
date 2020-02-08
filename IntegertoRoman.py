class Solution:
    


    def intToRoman(self, num: int) -> str:
        dict = {'1': 'I','2':'II','3':'III','4':'IV','5': 'V','6':'VI','7':'VII','8':'VIII','9':'IX',\
            '10': 'X','20':'XX','30':'XXX','40':'XL','50': 'L','60':'LX','70':'LXX','80':'LXXX','90':'XC',\
            '100': 'C','200':'CC','300':'CCC','400':'CD','500': 'D','600':'DC','700':'DCC','800':'DCCC','900':'CM',\
            '1000':'M','2000':'MM','3000':'MMM'}
        res=''
        str_num=str(num)
        i=len(str_num)-1
        while i>=0:
            if str_num[i]=='0':
                i-=1
                continue
            res=dict[str_num[i:]]+res
            str_num=str_num[:i]+'0'+str_num[i+1:]
            i-=1
        return res

s=Solution()
print(s.intToRoman(3000))