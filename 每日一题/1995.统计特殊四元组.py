#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#
from typing import List
# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j + 1,n):
                    for m in range(k + 1,n):
                        #print(nums[i] ,nums[j] , nums[k] ,nums[m])
                        if nums[i] + nums[j] + nums[k] == nums[m]:
                            res += 1
        return res 
# @lc code=end

Solution().countQuadruplets(nums = [1,1,1,3,5])