from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict={}
        for i in range(len(nums)):
            if target-nums[i] in mydict:
                res=list([i,mydict[target-nums[i]]])
                res.sort()
                return res
            else:
                mydict[nums[i]]=i

s=Solution()
s.twoSum([1,2,3],3)

