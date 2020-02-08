from typing import List
import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)<3:
            return []
        nums.sort()
        dist=sys.maxsize
        res=0
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                temp_sum=nums[i]+nums[L]+nums[R]
                temp=abs(temp_sum-target)
                if temp<dist:
                    res=nums[i]+nums[L]+nums[R]
                    dist=temp
                if temp_sum<target:
                    L+=1
                elif temp_sum>target:
                    R-=1
                else:
                    return temp_sum
        return res
s=Solution()
print(s.threeSumClosest([-1,0,1,1,55],3))