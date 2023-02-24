#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#
from typing import List
# @lc code=start
from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return  accumulate(nums)
# @lc code=end

