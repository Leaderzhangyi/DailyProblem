#
# @lc app=leetcode.cn id=2475 lang=python3
#
# [2475] 数组中不等三元组的数目
#

from typing import List
# @lc code=start
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n,ans=len(nums),0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]!=nums[j]:
                    for k in range(j+1,n):
                        if nums[j]!=nums[k] and nums[i]!=nums[k]:
                            ans+=1
        return ans
# @lc code=end

