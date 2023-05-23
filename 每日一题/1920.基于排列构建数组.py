#
# @lc app=leetcode.cn id=1920 lang=python3
#
# [1920] 基于排列构建数组
#
from typing import List

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for index,num in enumerate(nums):
            res.append(nums[nums[index]])
        return res 
# @lc code=end

print(Solution().buildArray([0,2,1,5,3,4]))