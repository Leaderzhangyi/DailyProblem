#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#
from typing import List
# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return str(grid).count("-")

# @lc code=end

