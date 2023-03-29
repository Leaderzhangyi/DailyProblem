#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
from typing import List
from itertools import combinations
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        #n = len(nums)
        res = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if abs(nums[i] - nums[j]) == k:
        #             res += 1
        for item in combinations(nums,2):
            if abs(item[0] - item[1]) == k:
                res += 1
        return res 


        
# @lc code=end

Solution().countKDifference(nums = [1,2,2,1], k = 1)