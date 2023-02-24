#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        return m * (co := sum(y & 1 for y in Counter(r[1] for r in indices).values())) + n * (ro := sum(x & 1 for x in Counter(r[0] for r in indices).values())) - co * ro * 2
        
# @lc code=end

