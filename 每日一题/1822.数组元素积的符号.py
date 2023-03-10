#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#
from typing import List
# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nn = len([i for i in nums if i < 0])
        zero = nums.count(0)
        if nn % 2 == 0 and zero == 0:
            return 1
        elif nn % 2 != 0 and zero == 0:
            return -1
        else:
            return 0
# @lc code=end

