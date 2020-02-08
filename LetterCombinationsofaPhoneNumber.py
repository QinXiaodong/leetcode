from typing import List
class Solution:
    mydict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ['']
        res=[]
        temp_res=self.letterCombinations(digits[1:])
        temp_str=self.mydict[digits[0]]
        for c in temp_str:
            for s in temp_res:
                res.append(c+s)
        return res
my_s=Solution()
print(my_s.letterCombinations('23'))