from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)<3:
            return []
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                if nums[i]+nums[L]+nums[R]==0:
                    res.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L]==nums[L+1]:
                        L+=1
                    while L<R and nums[R]==nums[R-1]:
                        R-=1
                    L=L+1
                    R=R-1
                elif nums[i]+nums[L]+nums[R]<0:
                    L+=1
                else:
                    R-=1
        return res
s=Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))